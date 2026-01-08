from fastapi import APIRouter, Depends, HTTPException

from app.Auth.core.dependencies import get_current_user
from app.web_builder.Recommendation.app.crud.crud import get_session, save_session
from app.web_builder.Recommendation.app.schemas.schema import *  # noqa: F401,F403
from app.web_builder.Recommendation.app.services.groq_service import groq_service
from app.web_builder.Recommendation.app.services.recommendation_service import (
    answer_and_generate_next_question,
    finalize_session,
    start_session,
    update_answer_and_regenerate,
)

router = APIRouter()


# 1️⃣ Generate Questions
@router.post("/generated_question")
def generated_question(
    data: StartRequest,
    user = Depends(get_current_user),
):
    session_id, questions = start_session(user, data)
    return {"session_id": session_id, "questions": questions}


@router.post("/next-question")
def next_question(
    data: NextQuestionRequest,
    user = Depends(get_current_user),
):
    try:
        question, total, completed = answer_and_generate_next_question(
            user=user,
            session_id=data.session_id,
            question_id=data.question_id,
            answer=data.answer,
        )
    except PermissionError:
        raise HTTPException(403, "Unauthorized session")
    except ValueError as exc:
        raise HTTPException(400, str(exc))

    return {
        "next_question": question,
        "questions_asked": total,
        "completed": completed,
    }


@router.post("/update-answer")
def update_answer(
    data: UpdateAnswerRequest,
    user = Depends(get_current_user),
):
    """
    Update a previously answered question and regenerate all subsequent questions.
    
    This allows users to go back and change their answers, with the system
    regenerating all questions that come after based on the new context.
    """
    try:
        question, total, completed = update_answer_and_regenerate(
            user=user,
            session_id=data.session_id,
            question_id=data.question_id,
            new_answer=data.new_answer,
        )
    except PermissionError:
        raise HTTPException(403, "Unauthorized session")
    except ValueError as exc:
        raise HTTPException(400, str(exc))

    return {
        "next_question": question,
        "questions_asked": total,
        "completed": completed,
    }



# 2️⃣ Color Palettes
@router.post("/color-palettes")
def color_palettes(
    data: PaletteRequest,
    user = Depends(get_current_user),
):
    # Extract user ID from User object
    user_id = user.user_id if hasattr(user, 'user_id') else user
    session = get_session(data.session_id)
    
    if not session:
        raise HTTPException(404, "Session not found")
        
    if session.get("user_id") != user_id:
        raise HTTPException(403, "Unauthorized")

    # Find the theme question answer (inspect stored question metadata)
    theme_answer = ""
    question_history = session.get("question_history", [])
    answers = session.get("answers", {})

    for entry in reversed(question_history):
        if groq_service.is_color_question(entry):
            answer = entry.get("answer")
            if answer is None:
                answer = answers.get(entry.get("id"))
            if isinstance(answer, (list, tuple, set)):
                theme_answer = ", ".join(str(item) for item in answer if item)
            else:
                theme_answer = str(answer or "").strip()
            if theme_answer:
                break

    # If no specific theme question found, use any answer as fallback
    if not theme_answer and answers:
        fallback_answer = next(iter(answers.values()))
        if isinstance(fallback_answer, (list, tuple, set)):
            theme_answer = ", ".join(str(item) for item in fallback_answer if item)
        else:
            theme_answer = str(fallback_answer or "").strip()

    # Generate dynamic color palettes using Groq
    business_type = session.get("business_type", "Business")
    prompt_context = session.get("prompt", theme_answer)

    palettes = groq_service.generate_color_palettes(
        theme_answer=theme_answer,
        business_type=business_type,
        prompt=prompt_context,
    )

    session["palettes"] = palettes
    save_session(data.session_id, session)
    return {"palettes": session["palettes"]}


# 4️⃣ Select Palette
@router.post("/select-palette")
def select_palette(
    data: SelectPaletteRequest,
    user = Depends(get_current_user),
):
    session = get_session(data.session_id)
    
    if not session:
        raise HTTPException(404, "Session not found")
    
    if "palettes" not in session:
        raise HTTPException(400, "No palettes generated. Call /color-palettes first.")

    selected = next(
        (p for p in session["palettes"] if p["id"] == data.palette_id),
        None,
    )

    if not selected:
        raise HTTPException(404, "Palette not found")

    session["selected_palette"] = selected
    save_session(data.session_id, session)
    return {"palette": selected}


# 5️⃣ Features
@router.post("/features")
def features(
    data: FeatureRequest,
    user = Depends(get_current_user),
):
    session = get_session(data.session_id)
    
    if not session:
        raise HTTPException(404, "Session not found")

    # Generate dynamic features using Groq based on user's prompt and answers
    prompt = session.get("prompt", "")
    business_type = session.get("business_type", "Business")
    answers = session.get("answers", {})

    features = groq_service.generate_features(prompt, business_type, answers)

    session["features"] = features
    save_session(data.session_id, session)
    return {"features": features}


# 6️⃣ Selected features
@router.post("/select_features")
def select_features(
    data: SelectFeaturesRequest,
    user = Depends(get_current_user),
):
    # Extract user ID from User object
    user_id = user.user_id if hasattr(user, 'user_id') else user
    session = get_session(data.session_id)
    
    if not session:
        raise HTTPException(404, "Session not found")

    if session.get("user_id") != user_id:
        raise HTTPException(403, "Unauthorized session")

    available_features = session.get("features", [])
    if not available_features:
        raise HTTPException(400, "No features generated for this session")

    selected_features = []
    for feature_ref in data.selected_features:
        selected = next(
            (f for f in available_features if f.get("id") == feature_ref),
            None,
        )
        if not selected and isinstance(feature_ref, str) and feature_ref.isdigit():
            idx = int(feature_ref) - 1
            if 0 <= idx < len(available_features):
                selected = available_features[idx]
        if selected:
            selected_features.append(selected)

    if not selected_features:
        raise HTTPException(404, "No valid features found")

    session["selected_features"] = selected_features
    save_session(data.session_id, session)
    return {"selected_features": selected_features}


# 7️⃣ Finalize
@router.post("/save_metadata")
def finalize(
    data: FinalizeRequest,
    user = Depends(get_current_user),
):
    # Extract user ID from User object
    user_id = user.user_id if hasattr(user, 'user_id') else user
    session = get_session(data.session_id)
    if not session:
        raise HTTPException(404, "Session not found")

    if session["user_id"] != user_id:
        raise HTTPException(403, "Unauthorized session")

    # Get selected features (IDs) from any possible key
    selected_feature_ids = (
        data.selected_features or 
        data.selectedFeatures or 
        data.feature_ids or 
        data.features
    )
    
    if not selected_feature_ids:
        # Fallback to session data (Redis) if previously saved via /select_features
        try:
            selected_features_objects = session.get("selected_features", [])
            selected_feature_ids = [
                f["id"] if isinstance(f, dict) else f 
                for f in selected_features_objects
            ]
        except:
            selected_feature_ids = []

    print(f"[API] 🎯 Finalizing with {len(selected_feature_ids) if selected_feature_ids else 0} features")

    metadata = finalize_session(
        user,
        data.session_id,
        selected_feature_ids,
        data.project_id,
    )
    return {"status": "completed", "metadata": metadata}