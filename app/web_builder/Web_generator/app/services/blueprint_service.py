"""
Blueprint Service - Main orchestrator for blueprint generation
Coordinates AI service and prompts to generate complete website blueprints

HYBRID APPROACH:
1. Business Templates → Select industry-appropriate templates
2. Industry Prompts → Enhanced AI prompts per business type
3. AI Content Generation → Creative, personalized content
4. Quality Validation → Ensure high-quality output
"""

import uuid
import json
import random
from typing import Dict, Any, List, Optional
from datetime import datetime

from app.web_builder.Web_generator.app.services.ai_service import AIService, get_ai_service
from app.web_builder.Web_generator.app.prompts.blueprint_prompts import BlueprintPrompts
from app.web_builder.Web_generator.app.prompts.color_library import ColorPaletteLibrary
from app.web_builder.Web_generator.app.prompts.industry_prompts import IndustryPrompts, QualityValidator
from app.web_builder.Web_generator.app.templates import BusinessTemplates
from app.web_builder.Web_generator.app.crud.crud import (
    get_session,
    save_blueprint_to_db,
    save_action_history_redis
)


class BlueprintService:
    """
    Service for generating rich website blueprints from metadata.
    
    HYBRID APPROACH:
    - Business Templates: Select industry-appropriate templates and configurations
    - Industry Prompts: Enhanced AI prompts tailored to business type
    - AI Content: Creative, personalized content generation
    - Quality Validation: Ensure output meets quality standards
    """
    
    def __init__(self, ai_service: Optional[AIService] = None):
        """
        Initialize Blueprint Service.
        
        Args:
            ai_service: Optional AI service instance. Uses singleton if not provided.
        """
        self.ai_service = ai_service or get_ai_service()
        self.prompts = BlueprintPrompts()
    
    def generate_blueprint(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate complete blueprint from metadata using HYBRID APPROACH.
        
        Flow:
        1. Validate metadata
        2. Extract business info & get industry config
        3. Build enhanced industry-specific AI prompt
        4. Call AI for content generation
        5. Apply business templates for structure
        6. Validate quality & auto-fix issues
        7. Save and return
        
        Args:
            metadata: Raw metadata from recommendation team
            
        Returns:
            Complete blueprint JSON with quality metrics
        """
        try:
            print(f"[BlueprintService] 🚀 Starting HYBRID blueprint generation...")
            
            # ============================================================
            # STEP 1: Validate metadata
            # ============================================================
            if not self._validate_metadata(metadata):
                return {"error": "Invalid metadata format"}
            
            # ============================================================
            # STEP 2: Extract key information
            # ============================================================
            session_id = metadata.get("session_id", str(uuid.uuid4()))
            business_data = metadata.get("business_extracted_data", {})
            questionnaire = metadata.get("questionnaire", {})
            design = metadata.get("design", {})
            user_prompt = metadata.get("user_prompt", "")
            
            # Get features from selected_features (user's choice) not all available features
            # Check multiple possible locations for selected_features
            selected_features = []
            
            # Path 1: original_session.questionnaire.selected_features
            original_session = metadata.get("original_session", {})
            original_questionnaire = original_session.get("questionnaire", {})
            if original_questionnaire.get("selected_features"):
                selected_features = original_questionnaire.get("selected_features", [])
                print(f"[BlueprintService] 📋 Found selected_features in original_session.questionnaire")
            
            # Path 2: questionnaire.selected_features (direct)
            elif questionnaire.get("selected_features"):
                selected_features = questionnaire.get("selected_features", [])
                print(f"[BlueprintService] 📋 Found selected_features in questionnaire")
            
            # Path 3: metadata.selected_features (root level)
            elif metadata.get("selected_features"):
                selected_features = metadata.get("selected_features", [])
                print(f"[BlueprintService] 📋 Found selected_features at root level")
            
            if selected_features:
                features = selected_features
                print(f"[BlueprintService] 📋 Using {len(features)} SELECTED features")
            else:
                features = metadata.get("features", [])
                print(f"[BlueprintService] 📋 Using {len(features)} available features (no selection found)")
            
            # Get business type and target audience
            business_type = business_data.get("business_type", "business")
            target_audience = business_data.get("target_audience", "")
            
            print(f"[BlueprintService] 📊 Business Type: {business_type}")
            print(f"[BlueprintService] 👥 Target Audience: {target_audience}")
            
            # ============================================================
            # STEP 3: Get industry-specific configuration
            # ============================================================
            business_config = BusinessTemplates.get_full_config(
                business_type=business_type,
                target_audience=target_audience
            )
            
            print(f"[BlueprintService] 🎨 Style: {business_config.get('style')}")
            print(f"[BlueprintService] 📝 Mood: {business_config.get('mood')}")
            
            # Get recommended hero variants for this business
            recommended_hero_variants = business_config.get("hero_variants", ["split-left-text"])
            recommended_fonts = business_config.get("fonts", {})
            animation_config = business_config.get("animation_config", {})
            
            # ============================================================
            # STEP 4: Build enhanced AI prompt with industry context
            # ============================================================
            # Use industry-specific system prompt
            system_prompt = IndustryPrompts.get_enhanced_system_prompt(business_type)
            
            # Add hero and about enhancements to user prompt
            hero_enhancement = IndustryPrompts.get_hero_enhancement(business_type, target_audience)
            about_enhancement = IndustryPrompts.get_about_enhancement(business_type)
            menu_enhancement = IndustryPrompts.get_menu_enhancement(business_type)
            testimonial_enhancement = IndustryPrompts.get_testimonial_enhancement(business_type)
            
            # NEW: Add audience-aware content enhancement
            audience_enhancement = IndustryPrompts.get_audience_enhanced_prompt(business_type, target_audience)
            
            # Build enhanced user prompt
            user_prompt_full = self._build_enhanced_prompt(
                metadata=metadata,
                business_config=business_config,
                hero_enhancement=hero_enhancement,
                about_enhancement=about_enhancement,
                menu_enhancement=menu_enhancement,
                testimonial_enhancement=testimonial_enhancement,
                recommended_hero_variants=recommended_hero_variants,
                recommended_fonts=recommended_fonts,
                audience_enhancement=audience_enhancement  # NEW: pass audience context
            )
            
            # ============================================================
            # STEP 5: Call AI service for content generation
            # ============================================================
            print(f"[BlueprintService] 🤖 Calling AI with industry-specific prompt...")
            ai_response = self.ai_service.generate_with_retry(
                system_prompt=system_prompt,
                user_prompt=user_prompt_full,
                max_retries=3,
                temperature=0.7,
                max_tokens=8000
            )
            
            if isinstance(ai_response, dict) and "projectName" in ai_response:
                print(f"[BlueprintService] ✅ AI response received (length: {len(str(ai_response))})")
            
            # ============================================================
            # STEP 6: Handle AI response or fallback
            # ============================================================
            if "error" in ai_response:
                print(f"[BlueprintService] ⚠️ AI Error: {ai_response['error']}")
                blueprint = self._generate_enhanced_fallback(metadata, business_config)
            elif not self.ai_service.validate_blueprint_response(ai_response):
                print("[BlueprintService] ⚠️ Invalid AI response, using enhanced fallback")
                blueprint = self._generate_enhanced_fallback(metadata, business_config)
            else:
                # Apply business templates to enhance AI response
                blueprint = self._apply_business_templates(
                    ai_response=ai_response,
                    business_config=business_config,
                    animation_config=animation_config
                )
            
            # ============================================================
            # STEP 7: Finalize blueprint with metadata
            # ============================================================
            blueprint = self._finalize_blueprint(
                ai_response=blueprint,
                metadata=metadata,
                session_id=session_id
            )
            
            # ============================================================
            # STEP 8: Quality validation & auto-fix
            # ============================================================
            validation = QualityValidator.validate(blueprint)
            print(f"[BlueprintService] 📊 Quality Score: {validation['score']}/100 ({QualityValidator.get_quality_grade(validation['score'])})")
            
            if validation["issues"]:
                print(f"[BlueprintService] ⚠️ Issues found: {len(validation['issues'])}")
                for issue in validation["issues"][:3]:
                    print(f"  - {issue}")
                
                # Auto-fix issues
                blueprint = QualityValidator.auto_fix(blueprint)
                print("[BlueprintService] 🔧 Applied auto-fixes")
            
            if validation["suggestions"]:
                print(f"[BlueprintService] 💡 Suggestions: {len(validation['suggestions'])}")
            
            # ============================================================
            # STEP 8.5: Fix component types based on IDs
            # ============================================================
            # AI sometimes returns generic types (Features, About) for specific features
            # This ensures the type matches the ID for proper template selection
            blueprint = self._fix_component_types(blueprint)
            print("[BlueprintService] 🔧 Fixed component types to match IDs")
            
            # ============================================================
            # STEP 8.6: Ensure all selected features have components
            # ============================================================
            # AI sometimes skips features - this adds missing ones
            blueprint = self._ensure_all_features_present(blueprint, features, business_data, metadata)
            
            # Add quality metrics to blueprint
            blueprint["quality"] = {
                "score": validation["score"],
                "grade": QualityValidator.get_quality_grade(validation["score"]),
                "issues_count": len(validation["issues"]),
                "suggestions_count": len(validation["suggestions"]),
                "generation_method": "hybrid_ai"
            }
            
            # ============================================================
            # STEP 9: Save to database
            # ============================================================
            blueprint_id = save_blueprint_to_db(session_id, blueprint)
            blueprint["blueprint_id"] = blueprint_id
            
            # Save action to Redis for undo/redo
            save_action_history_redis(session_id, {
                "action": "generate_blueprint",
                "blueprint_id": blueprint_id,
                "quality_score": validation["score"],
                "timestamp": datetime.now().isoformat()
            })
            
            print(f"[BlueprintService] ✅ Blueprint generated successfully!")
            print(f"[BlueprintService] 📋 ID: {blueprint_id} | Score: {validation['score']}/100")
            return blueprint
            
        except Exception as e:
            print(f"[BlueprintService] ❌ Error: {str(e)}")
            import traceback
            traceback.print_exc()
            return {"error": str(e)}
    
    def generate_blueprint_from_session(self, session_id: str) -> Dict[str, Any]:
        """
        Generate blueprint using session data from database.
        
        Args:
            session_id: Session ID to fetch metadata
            
        Returns:
            Complete blueprint JSON
        """
        session = get_session(session_id)
        if not session:
            return {"error": "Session not found"}
        
        # Convert session data to expected metadata format
        metadata = self._session_to_metadata(session, session_id)
        return self.generate_blueprint(metadata)
    
    # ============================================================
    # HYBRID APPROACH HELPER METHODS
    # ============================================================
    
    def _build_enhanced_prompt(
        self,
        metadata: Dict[str, Any],
        business_config: Dict[str, Any],
        hero_enhancement: str,
        about_enhancement: str,
        menu_enhancement: str,
        testimonial_enhancement: str,
        recommended_hero_variants: List[str],
        recommended_fonts: Dict[str, Any],
        audience_enhancement: str = ""  # NEW: audience context
    ) -> str:
        """
        Build enhanced user prompt with industry-specific context.
        
        Combines base blueprint prompt with:
        - Industry-specific content guidelines
        - Audience-aware tone adaptation
        - Recommended hero variants
        - Font recommendations
        - Section-specific tips
        """
        # Get base prompt from BlueprintPrompts
        base_prompt = self.prompts.get_full_blueprint_prompt(metadata)
        
        # Build enhancement section
        enhancements = f"""

=== INDUSTRY-SPECIFIC ENHANCEMENTS ===

{hero_enhancement}

{about_enhancement}

{menu_enhancement}

{testimonial_enhancement}

{audience_enhancement}

=== RECOMMENDED TEMPLATE SELECTIONS ===

HERO VARIANT OPTIONS (choose most appropriate):
{json.dumps(recommended_hero_variants)}

RECOMMENDED FONTS FOR THIS INDUSTRY:
Heading: {recommended_fonts.get('heading', {}).get('family', 'Inter')}
Body: {recommended_fonts.get('body', {}).get('family', 'Inter')}

BUSINESS STYLE: {business_config.get('style', 'modern')}
MOOD: {business_config.get('mood', 'Professional')}
AUDIENCE TONE: {business_config.get('audience_tone', 'professional and engaging')}

SPECIAL COMPONENTS TO INCLUDE:
{json.dumps(business_config.get('special_components', []))}

=== QUALITY REQUIREMENTS ===
1. Every section must have substantive content (no placeholders)
2. Hero headline: Max 10 words, powerful and memorable
3. About section: 3-4 well-crafted paragraphs with story arc
4. All descriptions: Specific and evocative, not generic
5. CTAs: Action-oriented, industry-appropriate text
6. Stats/Numbers: Realistic and impressive
7. USER INPUT IS SACRED: If user provided specific text, use it EXACTLY
"""
        
        return base_prompt + enhancements
    
    def _apply_business_templates(
        self,
        ai_response: Dict[str, Any],
        business_config: Dict[str, Any],
        animation_config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Apply business template configurations to AI-generated content.
        
        Enhances AI response with:
        - Industry-appropriate fonts
        - Curated animation settings
        - Style-matched effects
        """
        enhanced = ai_response.copy()
        
        # Apply recommended fonts if not already set properly
        fonts = business_config.get("fonts", {})
        if "globalStyles" not in enhanced:
            enhanced["globalStyles"] = {}
        
        if "typography" not in enhanced["globalStyles"]:
            enhanced["globalStyles"]["typography"] = {}
        
        typography = enhanced["globalStyles"]["typography"]
        if not typography.get("headingFont") or typography.get("headingFont", {}).get("family") == "Inter":
            typography["headingFont"] = fonts.get("heading", {"family": "Inter", "weights": [400, 600, 700]})
        if not typography.get("bodyFont") or typography.get("bodyFont", {}).get("family") == "Inter":
            typography["bodyFont"] = fonts.get("body", {"family": "Inter", "weights": [300, 400, 500]})
        
        typography["style"] = business_config.get("mood", "modern").lower()
        
        # Apply animation configuration to all components
        if animation_config and "components" in enhanced:
            for comp_key, comp in enhanced["components"].items():
                if isinstance(comp, dict):
                    if "animation" not in comp or not comp["animation"]:
                        comp["animation"] = animation_config.copy()
                    else:
                        # Merge with existing, keeping timing consistent
                        comp["animation"]["easing"] = animation_config.get("easing", "cubic-bezier(0.25, 1, 0.5, 1)")
        
        # Ensure effects are set
        if "effects" not in enhanced["globalStyles"]:
            enhanced["globalStyles"]["effects"] = {
                "glassmorphism": True,
                "gradients": True,
                "shadows": "elevated",
                "animations": "smooth-reveal"
            }
        
        # Add business context to theme
        if "theme" in enhanced:
            enhanced["theme"]["themeMood"] = business_config.get("mood", "Modern")
            if not enhanced["theme"].get("themeName"):
                enhanced["theme"]["themeName"] = f"{business_config.get('display_name', 'Custom')} Theme"
        
        return enhanced
    
    def _generate_enhanced_fallback(
        self,
        metadata: Dict[str, Any],
        business_config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate enhanced fallback blueprint using business templates.
        
        Used when AI fails, but produces better results than basic fallback
        by leveraging business-specific configurations.
        """
        print("[BlueprintService] 🔧 Generating enhanced fallback with business templates...")
        
        # Get basic fallback
        fallback = self._generate_fallback_blueprint(metadata)
        
        # Apply business template enhancements
        fallback = self._apply_business_templates(
            ai_response=fallback,
            business_config=business_config,
            animation_config=business_config.get("animation_config", {})
        )
        
        # Update theme mood
        if "theme" in fallback:
            fallback["theme"]["themeMood"] = business_config.get("mood", "Modern")
        
        # Add quality note
        fallback["quality"] = {
            "score": 65,
            "grade": "C+",
            "issues_count": 0,
            "suggestions_count": 1,
            "generation_method": "enhanced_fallback",
            "note": "Generated using fallback with business templates due to AI unavailability"
        }
        
        return fallback

    
    def _validate_metadata(self, metadata: Dict[str, Any]) -> bool:
        """
        Validate that metadata has minimum required fields.
        
        Args:
            metadata: Input metadata
            
        Returns:
            True if valid
        """
        # Check for essential fields (flexible validation)
        if not metadata:
            return False
        
        # At minimum, we need some business info or prompt
        has_business_data = bool(metadata.get("business_extracted_data"))
        has_prompt = bool(metadata.get("user_prompt"))
        has_questionnaire = bool(metadata.get("questionnaire"))
        
        return has_business_data or has_prompt or has_questionnaire
    
    def _session_to_metadata(self, session: Dict[str, Any], session_id: str) -> Dict[str, Any]:
        """
        Convert session data format to metadata format.
        Handles multiple formats including:
        1. Direct questionnaire format with answers array
        2. WizardData format with qa_data
        3. Legacy format with direct fields
        
        Args:
            session: Raw session data
            session_id: Session ID
            
        Returns:
            Formatted metadata
        """
        print(f"[BlueprintService] Converting session to metadata. Session keys: {list(session.keys())}")
        
        # ============================================
        # FORMAT 1: Questionnaire with answers (dict or array)
        # (from Recommendation team)
        # ============================================
        questionnaire = session.get("questionnaire", {})
        answers_raw = questionnaire.get("answers", {})
        
        # Handle answers in BOTH formats:
        # Format A: Dict {"q1": "value", "q2": "value"}
        # Format B: Array [{id: "q1", answer: "value"}, ...]
        answers_dict = {}
        
        if isinstance(answers_raw, dict):
            # Format A: Dictionary of answers
            for q_id, answer in answers_raw.items():
                if isinstance(answer, str):
                    answers_dict[q_id] = {"answer": answer, "question": ""}
                elif isinstance(answer, list):
                    # Handle checkbox/multi-select answers
                    answers_dict[q_id] = {"answer": answer, "question": ""}
                elif isinstance(answer, dict):
                    answers_dict[q_id] = answer
            print(f"[BlueprintService] 📋 Parsed answers from DICT format ({len(answers_dict)} answers)")
        elif isinstance(answers_raw, list):
            # Format B: Array of answer objects
            for ans in answers_raw:
                q_id = ans.get("question_id", ans.get("id", ""))
                answer = ans.get("answer", "")
                question = ans.get("question", "")
                answers_dict[q_id] = {"answer": answer, "question": question}
            print(f"[BlueprintService] 📋 Parsed answers from ARRAY format ({len(answers_dict)} answers)")
        
        # ============================================
        # FORMAT 2: WizardData format (legacy)
        # ============================================
        wizard_data = session.get("wizardData", session.get("wizard_data", {}))
        qa_data = wizard_data.get("qa_data", {})
        legacy_answers = qa_data.get("answers", session.get("answers", {}))
        
        # Merge legacy answers if no questionnaire format
        if not answers_dict and legacy_answers:
            if isinstance(legacy_answers, dict):
                answers_dict = {k: {"answer": v, "question": ""} for k, v in legacy_answers.items()}
                print(f"[BlueprintService] 📋 Using legacy answers ({len(answers_dict)} answers)")
        
        # ============================================
        # Extract User Prompt
        # ============================================
        user_prompt = (
            session.get("user_prompt") or 
            questionnaire.get("prompt") or 
            qa_data.get("initial_prompt") or 
            session.get("prompt") or
            ""
        )
        print(f"[BlueprintService] User prompt: {user_prompt}")
        
        # ============================================
        # NEW: Extract answers using prop_key mapping
        # This is the key to proper answer → template prop mapping
        # ============================================
        prop_answers = {}
        questions_list = questionnaire.get("questions", [])
        
        # Build prop_key → answer mapping from questions with prop_key
        for q in questions_list:
            prop_key = q.get("prop_key")
            q_id = q.get("id")
            
            if prop_key and q_id:
                # Get answer from answers_dict
                ans_data = answers_dict.get(q_id, answers_raw.get(q_id, {}))
                
                if isinstance(ans_data, dict):
                    answer = ans_data.get("answer", "")
                elif isinstance(ans_data, (str, list)):
                    answer = ans_data
                else:
                    answer = ""
                
                if answer:
                    prop_answers[prop_key] = answer
                    print(f"[BlueprintService] 📋 prop_key '{prop_key}' = {str(answer)[:50]}...")
        
        print(f"[BlueprintService] ✅ Extracted {len(prop_answers)} prop_key based answers")
        
        # ============================================
        # Extract Business Name - priority to prop_key
        # ============================================
        business_name = (
            prop_answers.get("businessName") or
            answers_dict.get("q1", {}).get("answer") if isinstance(answers_dict.get("q1", {}), dict) else answers_dict.get("q1") or
            ""
        )
        
        # Handle dict answer format
        if isinstance(business_name, dict):
            business_name = business_name.get("answer", "")
        
        # Capitalize and clean the business name
        if business_name:
            business_name = str(business_name).strip().title()
            print(f"[BlueprintService] 🏢 Business Name: {business_name}")
        
        # ============================================
        # Extract Hero content from prop_key answers
        # ============================================
        hero_title = prop_answers.get("title", "")
        hero_subtitle = prop_answers.get("subtitle", "")
        
        if hero_title:
            print(f"[BlueprintService] 🎯 Hero Title from user: {hero_title}")
        if hero_subtitle:
            print(f"[BlueprintService] 🎯 Hero Subtitle from user: {hero_subtitle}")
        
        # ============================================
        # Extract ALL prop_key answers for different website types
        # ============================================
        # Common answers
        cta = prop_answers.get("cta", "Get Started")
        story = prop_answers.get("story", "")
        color_theme = prop_answers.get("colorTheme", "")
        
        # Cafe/Restaurant specific
        signature = prop_answers.get("signature", "")  # Bestseller item
        cuisine = prop_answers.get("cuisine", "")  # Food type
        atmosphere = prop_answers.get("atmosphere", "")  # Vibe
        menu_items = prop_answers.get("menuItems", [])  # Menu categories
        hours = prop_answers.get("hours", "")  # Opening hours
        specialty = prop_answers.get("specialty", "")  # Type of cafe
        location = prop_answers.get("location", "")  # Address
        
        # Agency specific
        services_answer = prop_answers.get("services", [])
        approach = prop_answers.get("approach", "")
        client_type = prop_answers.get("clientType", [])
        
        # Portfolio specific  
        profession = prop_answers.get("profession", "")
        skills = prop_answers.get("skills", [])
        work_style = prop_answers.get("workStyle", "")
        experience = prop_answers.get("experience", "")
        
        # Gaming specific
        game_name = prop_answers.get("gameName", "")
        genre = prop_answers.get("genre", [])
        platforms = prop_answers.get("platforms", [])
        game_style = prop_answers.get("style", "")
        game_features = prop_answers.get("features", [])
        
        # Ecommerce specific
        product_type = prop_answers.get("productType", "")
        usp = prop_answers.get("usp", "")
        shipping = prop_answers.get("shipping", [])
        
        # Log all extracted answers
        print(f"[BlueprintService] 📋 Extracted {len(prop_answers)} prop_key answers")
        
        # ============================================
        # Fallback: Extract from fixed q1-q10 if no prop_key
        # (Legacy support for old sessions)
        # ============================================
        def get_answer(q_id, default=""):
            ans = answers_dict.get(q_id, {})
            if isinstance(ans, dict):
                return ans.get("answer", default)
            elif isinstance(ans, str):
                return ans
            elif isinstance(ans, list):
                return ans  # For checkbox/multi-select
            return default
        
        # Only use fixed mappings as fallback
        if not business_name:
            business_name = get_answer("q1", "")
        if not color_theme:
            color_theme = get_answer("q2", "Blue")
        
        target_audience = get_answer("q1", "General audience")
        primary_goal = get_answer("q3", "Online presence") if not services_answer else str(services_answer)
        ecommerce = get_answer("q4", "no")
        layout_pref = get_answer("q5", "Modern")
        blog_section = get_answer("q6", "no")
        navigation_style = get_answer("q7", "Standard")
        auth_needed = get_answer("q8", "no")
        font_style = get_answer("q9", "Modern")
        highlight_features = get_answer("q10", "Services")
        
        print(f"[BlueprintService] Extracted - Business: {business_name}, Color: {color_theme}")
        
        # ============================================
        # Extract Colors from Selected Palette
        # ============================================
        colors = []
        
        # Try 1: questionnaire.selected_palette
        selected_palette = questionnaire.get("selected_palette", {})
        if selected_palette and "colors" in selected_palette:
            palette_colors = selected_palette["colors"]
            for c in palette_colors:
                if isinstance(c, str):
                    colors.append(c)
                elif isinstance(c, dict) and "hex" in c:
                    colors.append(c["hex"])
            print(f"[BlueprintService] 🎨 Colors from questionnaire.selected_palette")
        
        # Try 2: questionnaire.palettes (first generated palette)
        if not colors:
            palettes = questionnaire.get("palettes", [])
            if palettes and len(palettes) > 0:
                first_palette = palettes[0]
                if "colors" in first_palette:
                    colors = first_palette["colors"]
                    print(f"[BlueprintService] 🎨 Colors from questionnaire.palettes[0]: {first_palette.get('title', '')}")
        
        # Try 3: design.selected_palette
        if not colors:
            design_palette = session.get("design", {}).get("selected_palette", {})
            if design_palette and "colors" in design_palette:
                for c in design_palette["colors"]:
                    if isinstance(c, str):
                        colors.append(c)
                    elif isinstance(c, dict) and "hex" in c:
                        colors.append(c["hex"])
                print(f"[BlueprintService] 🎨 Colors from design.selected_palette")
        
        # Try 4: wizard_data.color_combination
        if not colors:
            color_combo = wizard_data.get("color_combination", session.get("color_combination", {}))
            if color_combo and "colors" in color_combo:
                for c in color_combo["colors"]:
                    if isinstance(c, dict) and "hex" in c:
                        colors.append(c["hex"])
                print(f"[BlueprintService] 🎨 Colors from wizard_data.color_combination")
        
        # ============================================
        # HIGHEST PRIORITY: User's color theme TEXT choice
        # This OVERRIDES any selected palette because user explicitly chose this
        # ============================================
        if color_theme:
            t = color_theme.lower()
            theme_colors = None
            
            if "dark" in t:
                # User wants dark mode - background MUST be dark (index 4)
                theme_colors = ["#7C3AED", "#10B981", "#F59E0B", "#1F2937", "#0F172A"]
                print(f"[BlueprintService] 🎨 User selected DARK MODE - using dark color palette")
            elif "bold" in t or "creative" in t or "vibrant" in t:
                theme_colors = ["#FF6B6B", "#4ECDC4", "#FFE66D", "#F1F5F9", "#FFFFFF"]
                print(f"[BlueprintService] 🎨 User selected BOLD/CREATIVE - using vibrant colors")
            elif "minimal" in t or ("clean" in t):
                theme_colors = ["#1E293B", "#64748B", "#3B82F6", "#F8FAFB", "#FFFFFF"]
                print(f"[BlueprintService] 🎨 User selected CLEAN MINIMAL - using minimal colors")
            elif "professional" in t or "navy" in t or "trustworthy" in t:
                theme_colors = ["#1E3A5F", "#64748B", "#3B82F6", "#F1F5F9", "#FFFFFF"]
                print(f"[BlueprintService] 🎨 User selected PROFESSIONAL - using navy colors")
            elif "warm" in t or "espresso" in t or "cozy" in t:
                theme_colors = ["#8B4513", "#D2691E", "#F5DEB3", "#FFFDF9", "#FCF5E5"]
                print(f"[BlueprintService] 🎨 User selected WARM - using warm earth tones")
            elif "neon" in t or "cyber" in t or "futuristic" in t:
                theme_colors = ["#00F0FF", "#FF00E4", "#00FF88", "#1A1A2E", "#0A0A1A"]
                print(f"[BlueprintService] 🎨 User selected NEON/CYBER - using neon colors")
            elif "retro" in t or "arcade" in t:
                theme_colors = ["#FF6B9D", "#FFE93E", "#9D4EDD", "#2E1A47", "#1A0A2E"]
                print(f"[BlueprintService] 🎨 User selected RETRO - using arcade colors")
            elif "esports" in t or "pro gamer" in t:
                theme_colors = ["#00FF00", "#1DB954", "#FF4500", "#121212", "#0A0A0A"]
                print(f"[BlueprintService] 🎨 User selected ESPORTS - using gaming colors")
            elif "gold" in t or "elegant" in t or "luxury" in t:
                theme_colors = ["#D4AF37", "#FFFFFF", "#F5E6C8", "#1A1A1A", "#0F0F0F"]
                print(f"[BlueprintService] 🎨 User selected ELEGANT/GOLD - using luxury colors")
            elif "blue" in t and "green" in t:
                theme_colors = ["#0077B6", "#00B4D8", "#4CAF50", "#F8FAFC", "#1E293B"]
            elif "blue" in t or "ocean" in t:
                theme_colors = ["#1E40AF", "#3B82F6", "#F59E0B", "#F8FAFC", "#1E293B"]
            elif "green" in t or "garden" in t or "fresh" in t or "eco" in t:
                theme_colors = ["#10B981", "#059669", "#3B82F6", "#F8FAFC", "#0F172A"]
            elif "orange" in t or "terracotta" in t:
                theme_colors = ["#E67E22", "#D35400", "#27AE60", "#FFFAF5", "#2C2C2C"]
            elif "purple" in t or "tech" in t:
                theme_colors = ["#8B5CF6", "#7C3AED", "#10B981", "#0F172A", "#F8FAFC"]
            elif "coral" in t or "pink" in t or "rose" in t:
                theme_colors = ["#FF6B6B", "#FCA5A5", "#10B981", "#FFF5F5", "#1A1A2E"]
            elif "red" in t:
                theme_colors = ["#E50914", "#B81D24", "#F5F5F1", "#0A0A0A", "#FFFFFF"]
            
            if theme_colors:
                colors = theme_colors  # Override any previously set colors
                print(f"[BlueprintService] 🎨 Using user's color theme choice: {color_theme}")
            else:
                # If no specific theme color recognized, but they gave a description,
                # use it to pick a palette from the library
                detected_type = self._extract_business_type(user_prompt or color_theme)
                palette = ColorPaletteLibrary.get_safe_palette_for_industry(detected_type)
                colors = [
                    palette["primary"], 
                    palette["secondary"], 
                    palette["accent"], 
                    palette["surface"],
                    palette["background"]
                ]
                print(f"[BlueprintService] 🎨 Using industry-matched palette for: {detected_type}")

        # Default colors if none found - use validated palettes
        if not colors:
            # Detect business type again for color selection
            detected_type = self._extract_business_type(user_prompt)
            # Use the new safe palette method that guarantees good contrast
            palette = ColorPaletteLibrary.get_safe_palette_for_industry(detected_type)
            colors = [
                palette["primary"], 
                palette["secondary"], 
                palette["accent"], 
                palette["surface"],
                palette["background"]
            ]
            print(f"[BlueprintService] 🎨 No color choice found, using default {detected_type} palette")
        
        print(f"[BlueprintService] 🎨 Final colors: {colors[:3]}...")
        
        # ============================================
        # Extract Features
        # ============================================
        features = []
        
        # Priority 1: From questionnaire.selected_features (object list)
        selected_features = questionnaire.get("selected_features", [])
        if not selected_features:
            # Check session level selected_features
            selected_features = session.get("selected_features", [])
            
        if selected_features:
            features = [
                f.get("name", f.get("id", f)) if isinstance(f, dict) else f 
                for f in selected_features
            ]
            print(f"[BlueprintService] 🎯 Found {len(features)} SELECTED features")
        
        # Priority 2: From session.features (string list) fallback only if no selection
        if not features:
            session_features = session.get("features", [])
            if session_features:
                features = [f if isinstance(f, str) else f.get("name", "") for f in session_features]
                print(f"[BlueprintService] ⚠️ No selection found, using {len(features)} available features")
        
        # Priority 3: From wizard_data.selected_pages
        if not features:
            selected_pages = wizard_data.get("selected_pages", session.get("selected_pages", []))
            if selected_pages:
                features = [page.get("name", page.get("id", "")) for page in selected_pages]
        
        # Priority 4: Default minimal features
        if not features:
            features = ["Home", "About", "Contact"]
            if blog_section.lower() == "yes":
                features.append("Blog")
            if auth_needed.lower() == "yes":
                features.append("Authentication")
            if highlight_features:
                features.append(highlight_features)
            print(f"[BlueprintService] ⚠️ Using default minimal features: {features}")
        
        # Self-Correction: If we have multiple Q&A answers but no FAQ in features, ADD IT
        if "FAQ" not in [f.upper() for f in features]:
            faq_potential_answers = [a for k, a in answers_dict.items() if ("q" in k.lower() or "faq" in k.lower()) and len(str(a)) > 5]
            if len(faq_potential_answers) >= 2 or questionnaire.get("faqs"):
                features.append("FAQ")
                print(f"[BlueprintService] ➕ Auto-added FAQ to features due to detected QA content")

        print(f"[BlueprintService] Extracted features: {features}")
        
        # ============================================
        # Determine Business Type from Prompt
        # ============================================
        business_type = self._extract_business_type(user_prompt)
        print(f"[BlueprintService] Detected business type: {business_type}")
        
        # ============================================
        # Extract Style Preferences
        # ============================================
        style_preferences = []
        if layout_pref:
            style_preferences.append(layout_pref)
        if navigation_style:
            style_preferences.append(f"{navigation_style} navigation")
        if font_style:
            style_preferences.append(f"{font_style} fonts")
        if not style_preferences:
            style_preferences = ["Modern"]
        
        # ============================================
        # Build Questionnaire Questions for AI
        # ============================================
        questionnaire_questions = []
        for q_id, data in answers_dict.items():
            questionnaire_questions.append({
                "id": q_id,
                "type": "input",
                "question": data.get("question", f"Question {q_id}"),
                "user_answer": data.get("answer", "")
            })
        
        # ============================================
        # Build Final Metadata
        # ============================================
        metadata = {
            "session_id": session_id,
            "timestamp": datetime.now().isoformat(),
            "user_prompt": user_prompt,
            "business_name": business_name,  # Extracted business name
            
            # prop_key based answers for direct template mapping
            "prop_answers": prop_answers,
            
            # User's exact hero content
            "user_hero": {
                "title": hero_title,
                "subtitle": hero_subtitle,
                "cta": cta,
            },
            
            # User's services if provided (for agency/corporate)
            "user_services": services_answer if isinstance(services_answer, list) else [],
            
            # CAFE/RESTAURANT specific data
            "cafe_data": {
                "signature": signature,  # Bestseller item - USE THIS IN MENU!
                "cuisine": cuisine,
                "atmosphere": atmosphere,
                "menu_items": menu_items if isinstance(menu_items, list) else [],
                "hours": hours,
                "specialty": specialty,
                "location": location,
            },
            
            # GAMING specific data
            "gaming_data": {
                "game_name": game_name,
                "genre": genre if isinstance(genre, list) else [],
                "platforms": platforms if isinstance(platforms, list) else [],
                "style": game_style,
                "features": game_features if isinstance(game_features, list) else [],
            },
            
            # PORTFOLIO specific data
            "portfolio_data": {
                "profession": profession,
                "skills": skills if isinstance(skills, list) else [],
                "work_style": work_style,
                "experience": experience,
            },
            
            # ECOMMERCE specific data
            "ecommerce_data": {
                "product_type": product_type,
                "usp": usp,
                "shipping": shipping if isinstance(shipping, list) else [],
            },
            
            "business_extracted_data": {
                "business_type": business_type,
                "industry": business_type,
                "business_name": business_name,
                "target_audience": target_audience,
                "goals": primary_goal,
                "services": services_answer if isinstance(services_answer, list) else [],
                "style_preferences": style_preferences,
                "work_style": work_style,
                "approach": approach,
                "story": story,
                "signature_item": signature,  # Include for all types
                "requires_ecommerce": ecommerce.lower() == "yes" if isinstance(ecommerce, str) else False,
                "requires_blog": blog_section.lower() == "yes" if isinstance(blog_section, str) else False,
                "requires_auth": auth_needed.lower() == "yes" if isinstance(auth_needed, str) else False,
                "highlight_feature": highlight_features
            },
            "questionnaire": {
                "questions": questionnaire_questions,
                "raw_answers": answers_dict,
                "prop_answers": prop_answers,  # NEW: Include for template rendering
            },
            "design": {
                "selected_palette": {
                    "id": "custom",
                    "colors": colors
                },
                "color_theme_text": color_theme,  # NEW: User's color preference text
                "font_style": font_style,
                "navigation_style": navigation_style
            },
            "features": features,
            "final_metadata_ready": True,
            # Preserve original session data
            "original_session": session
        }
        
        print(f"[BlueprintService] ✅ Metadata conversion complete.")
        print(f"[BlueprintService] 📋 Business: {business_name or business_type}")
        print(f"[BlueprintService] 🎯 Hero Title: {hero_title or '(not provided)'}")
        print(f"[BlueprintService] 🎯 Hero Subtitle: {hero_subtitle or '(not provided)'}")
        print(f"[BlueprintService] 🎨 Color Theme: {color_theme}")
        return metadata
    
    def _extract_business_type(self, prompt: str) -> str:
        """
        Extract business type from user prompt.
        Ensures it matches keys in WEBSITE_TYPE_TEMPLATES.
        """
        if not prompt:
            return "agency"
            
        prompt_lower = prompt.lower()
        
        business_keywords = {
            "restaurant": ["restaurant", "food", "dining", "eatery", "cuisine", "kitchen", "bistro", "steakhouse"],
            "bakery": ["bakery", "bake", "cake", "pastry", "bread", "sweets", "donut"],
            "cafe": ["coffee", "espresso", "cafe", "barista", "beans", "brew", "latte"],
            "ecommerce": ["store", "shop", "retail", "boutique", "fashion", "clothing", "apparel", "ecommerce", "buy", "sell"],
            "gaming": ["gaming", "game", "esports", "gamer", "play", "match", "console", "pc games", "tournament", "steam", "twitch"],
            "movie": ["movie", "cinema", "theater", "theatre", "film", "screen", "box office", "blockbuster", "showtime"],
            "portfolio": ["portfolio", "personal", "developer", "designer", "freelance", "photographer", "cv", "resume"],
            "agency": ["agency", "marketing", "design", "creative", "consulting", "branding", "corporate", "business"],
            "healthcare": ["clinic", "doctor", "medical", "health", "dental", "physio", "hospital"],
            "fitness": ["gym", "fitness", "yoga", "workout", "training", "crossfit", "athletics", "personal trainer"],
            "education": ["school", "education", "tutoring", "learning", "academy", "course", "college", "university"],
            "technology": ["tech", "software", "app", "startup", "IT", "digital", "coding", "saas", "platform"]
        }
        
        # Priority 1: Check for exact keyword matches
        for b_type, keywords in business_keywords.items():
            for keyword in keywords:
                if keyword in prompt_lower:
                    return b_type
        
        # Priority 2: Check for name patterns
        if "gam" in prompt_lower:
            return "gaming"
        if "film" in prompt_lower or "cine" in prompt_lower:
            return "movie"
        if "shop" in prompt_lower or "store" in prompt_lower:
            return "ecommerce"
        if "food" in prompt_lower or "eat" in prompt_lower:
            return "restaurant"
            
        return "agency"
    
    def _finalize_blueprint(
        self, 
        ai_response: Dict[str, Any], 
        metadata: Dict[str, Any],
        session_id: str
    ) -> Dict[str, Any]:
        """
        Finalize and enhance AI-generated blueprint.
        
        Args:
            ai_response: Raw AI response
            metadata: Original metadata
            session_id: Session ID
            
        Returns:
            Finalized blueprint
        """
        # Add project identifiers
        ai_response["projectId"] = str(uuid.uuid4())
        ai_response["session_id"] = session_id
        ai_response["created_at"] = datetime.now().isoformat()
        
        # FIX for HTMLGeneratorService compatibility
        # Ensure 'websiteType' matches 'projectType'
        if "projectType" in ai_response:
            ai_response["websiteType"] = ai_response["projectType"]
        elif "business_extracted_data" in metadata:
            ai_response["websiteType"] = metadata["business_extracted_data"].get("business_type", "agency")
        
        # Preserve original metadata
        ai_response["metadata"] = metadata
        
        # Ensure SEO exists
        if "seo" not in ai_response:
            business_name = ai_response.get("projectName", "Website")
            ai_response["seo"] = {
                "title": f"{business_name} - Official Website",
                "description": f"Welcome to {business_name}. Discover our services and offerings.",
                "keywords": [business_name.lower(), "services", "contact"]
            }
        
        # Ensure globalStyles exists
        if "globalStyles" not in ai_response:
            ai_response["globalStyles"] = self._get_default_global_styles(
                metadata.get("business_extracted_data", {}).get("style_preferences", ["Modern"])
            )
        
        # Ensure designVision exists
        if "designVision" not in ai_response:
            ai_response["designVision"] = {
                "design_theme": "modern",
                "hero_concept": "A visually striking hero section with bold typography and smooth animations",
                "visual_personality": "Clean, professional, and engaging"
            }
        
        # Add component order (ensure FAQ is included if it exists in components but not order)
        components = ai_response.get("components", {})
        order = ai_response.get("componentOrder", list(components.keys()))
        
        # Self-correction: ensure FAQ is in order if FAQ component exists
        for comp_key in components:
            if "faq" in comp_key.lower() and comp_key not in order:
                order.append(comp_key)
        
        ai_response["componentOrder"] = order
        
        # Assign random layout variants if missing
        self._ensure_layout_variants(ai_response)
        
        return ai_response
    
    def _ensure_layout_variants(self, blueprint: Dict[str, Any]) -> None:
        """
        Ensure all components have layout variants assigned.
        
        Args:
            blueprint: Blueprint to enhance (modified in place)
        """
        layout_variants = self.prompts.get_layout_variants()
        
        for comp_key, component in blueprint.get("components", {}).items():
            if not isinstance(component, dict):
                continue
                
            props = component.get("props", {})
            comp_type = component.get("type", "")
            
            # If no layout variant, assign random one
            if "layoutVariant" not in props and comp_type in layout_variants:
                props["layoutVariant"] = random.choice(layout_variants[comp_type])
                component["props"] = props
    
    def _get_default_global_styles(self, style_preferences: List[str]) -> Dict[str, Any]:
        """
        Get default global styles based on preferences.
        
        Args:
            style_preferences: List of style preferences
            
        Returns:
            GlobalStyles object
        """
        # Determine mood from preferences
        mood = "Modern"
        for pref in style_preferences:
            if pref.lower() in ["premium", "elegant", "luxury"]:
                mood = "Premium"
            elif pref.lower() in ["warm", "friendly", "cozy"]:
                mood = "Warm"
            elif pref.lower() in ["playful", "fun", "vibrant"]:
                mood = "Playful"
            elif pref.lower() in ["professional", "corporate", "formal"]:
                mood = "Professional"
        
        # Get font pairing for mood
        font_pairings = self.prompts.get_font_pairings()
        fonts = font_pairings.get(mood, font_pairings["Modern"])
        
        return {
            "typography": {
                "headingFont": fonts["headingFont"],
                "bodyFont": fonts["bodyFont"],
                "style": mood.lower()
            },
            "spacing": {
                "sectionGap": "100px",
                "containerMaxWidth": "1280px"
            },
            "effects": {
                "glassmorphism": True,
                "gradients": True,
                "shadows": "elevated",
                "animations": "smooth-reveal"
            },
            "animationConfig": {
                "easing": "cubic-bezier(0.25, 1, 0.5, 1)",
                "hoverEffect": "magnetic-cursor" if mood == "Premium" else "scale"
            }
        }
    
    def _generate_fallback_blueprint(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a basic blueprint without AI when AI fails.
        Uses rule-based generation.
        
        Args:
            metadata: Input metadata
            
        Returns:
            Basic blueprint
        """
        print("[BlueprintService] Using fallback blueprint generation")
        
        business_data = metadata.get("business_extracted_data", {})
        design = metadata.get("design", {})
        features = metadata.get("features", ["Home", "About", "Contact"])
        questionnaire = metadata.get("questionnaire", {})
        original_session = metadata.get("original_session", {})
        
        # ============================================
        # Extract business name from multiple sources
        # ============================================
        business_name = (
            metadata.get("business_name") or  # First: from our metadata conversion
            business_data.get("business_name") or  # Second: from business_extracted_data
            ""
        )
        
        # Try to get from questionnaire answers if still empty
        if not business_name:
            # Check questionnaire.answers (dict format: {"q1": "value"})
            answers = questionnaire.get("answers", {})
            if isinstance(answers, dict):
                q1 = answers.get("q1", "")
                if isinstance(q1, str):
                    business_name = q1.strip().title()
                elif isinstance(q1, dict):
                    business_name = q1.get("answer", "").strip().title()
            
            # Check original_session.questionnaire.answers
            if not business_name:
                orig_questionnaire = original_session.get("questionnaire", {})
                orig_answers = orig_questionnaire.get("answers", {})
                if isinstance(orig_answers, dict):
                    q1 = orig_answers.get("q1", "")
                    if isinstance(q1, str):
                        business_name = q1.strip().title()
        
        # Fallback to user prompt if still empty
        if not business_name:
            user_prompt = metadata.get("user_prompt", "")
            # Try to extract from prompt like "cafe website for X"
            business_name = "Your Business"
        
        tagline = ""
        
        # Extract tagline from questions if available
        questions = questionnaire.get("questions", [])
        for q in questions:
            answer = q.get("user_answer", "")
            q_text = q.get("question", "").lower()
            if "tagline" in q_text or q.get("id") == "q2":
                tagline = answer
        
        business_type = business_data.get("business_type", "Business")
        industry = business_data.get("industry", "General")
        
        print(f"[BlueprintService] 🏢 Fallback using: {business_name} ({business_type})")
        
        # Get colors - use our properly extracted colors from design
        palette = design.get("selected_palette", {})
        colors = palette.get("colors", ["#4F46E5", "#10B981", "#F59E0B", "#FFFFFF"])
        
        # Build components
        components = {}
        component_order = []
        
        # Map features to components - enhanced for cafe/restaurant specific features
        feature_mapping = {
            # Standard features
            "home": "Home",
            "hero": "Home",
            "about": "About",
            "our story": "About",
            "about us": "About",
            
            # Menu variations (for restaurants/cafes)
            "menu": "Menu",
            "our menu": "Menu",
            "food menu": "Menu",
            
            # Specials (for restaurants/cafes)
            "specials": "Specials",
            "today's specials": "Specials", 
            "daily specials": "Specials",
            
            # Hours/Location (for local businesses)
            "hours": "Hours",
            "hours & location": "Hours",
            "location": "Hours",
            "hours and location": "Hours",
            "opening hours": "Hours",
            
            # Standard business features
            "services": "Services",
            "our services": "Services",
            "features": "Features",
            "gallery": "Gallery",
            "photos": "Gallery",
            "testimonials": "Testimonials",
            "reviews": "Testimonials",
            "customer love": "Testimonials",
            "contact": "Contact",
            "contact us": "Contact",
            "get in touch": "Contact",
            "online ordering": "CTA",
            "order online": "CTA",
            "pricing": "Pricing",
            "prices": "Pricing",
            "team": "Team",
            "our team": "Team",
            "faq": "FAQ",
            "cta": "CTA",
            "call to action": "CTA"
        }
        
        # Always add Home first
        home_key = "comp-home"
        components[home_key] = {
            "id": "home",
            "type": "Home",
            "name": "Home Section",
            "props": {
                "layoutVariant": random.choice(BlueprintPrompts.get_layout_variants()["Hero"]),
                "title": f"Welcome to {business_name}",
                "subtitle": tagline or f"Your trusted {business_type.lower()} partner",
                "description": f"Experience the best {industry.lower()} services tailored just for you.",
                "cta": "Get Started",
                "ctaSecondary": "Learn More",
                "backgroundStyle": "gradient-mesh"
            },
            "animation": {
                "type": "reveal-mask",
                "duration": 1000,
                "delay": 0,
                "easing": "cubic-bezier(0.25, 1, 0.5, 1)"
            }
        }
        component_order.append(home_key)
        
        # Add other sections based on features
        for feature in features:
            feature_lower = feature.lower()
            if feature_lower == "home":
                continue  # Already added as Home
                
            comp_type = feature_mapping.get(feature_lower, "Features")
            comp_id = feature_lower.replace(" ", "_")
            comp_key = f"comp-{comp_id}"
            
            if comp_key not in components:
                components[comp_key] = self._create_fallback_component(
                    comp_id=comp_id,
                    comp_type=comp_type,
                    business_name=business_name,
                    business_type=business_type,
                    services=business_data.get("services", [])
                )
                component_order.append(comp_key)
        
        # Always add Contact if not present
        if "comp-contact" not in components:
            components["comp-contact"] = self._create_fallback_component(
                comp_id="contact",
                comp_type="Contact",
                business_name=business_name,
                business_type=business_type,
                services=[]
            )
            component_order.append("comp-contact")
        
        # Build navigation
        nav_links = []
        for comp_key in component_order:
            if comp_key == "comp-hero":
                continue
            comp = components[comp_key]
            nav_links.append({
                "label": comp["name"].replace(" Section", ""),
                "href": f"#{comp['id']}"
            })
        
        return {
            "projectId": str(uuid.uuid4()),
            "projectName": business_name,
            "projectType": business_type.lower(),
            "session_id": metadata.get("session_id", str(uuid.uuid4())),
            "created_at": datetime.now().isoformat(),
            "metadata": metadata,
            "seo": {
                "title": f"{business_name} | {industry}",
                "description": f"{business_name} offers top-quality {business_type.lower()} services. Contact us today!",
                "keywords": [business_name.lower(), business_type.lower(), industry.lower()]
            },
            "theme": {
                "themeName": "Custom Theme",
                "themeMood": "Modern",
                "primaryColor": colors[0] if colors else "#4F46E5",
                "colorSchemeType": "Custom",
                "colorPalette": {
                    "primary": colors[0] if colors else "#4F46E5",
                    "secondary": colors[1] if len(colors) > 1 else "#10B981",
                    "accent": colors[2] if len(colors) > 2 else "#F59E0B",
                    "background": colors[3] if len(colors) > 3 else "#FFFFFF",
                    "surface": "#F5F5F5",
                    "text": "#1A1A1A"
                },
                "gradients": {
                    "hero": f"linear-gradient(135deg, {colors[0]}20, {colors[1] if len(colors) > 1 else colors[0]}20)",
                    "accent": f"linear-gradient(90deg, {colors[0]}, {colors[2] if len(colors) > 2 else colors[0]})"
                }
            },
            "components": components,
            "componentOrder": component_order,
            "navigation": {
                "header": {
                    "logo": {"text": business_name, "style": "modern"},
                    "links": nav_links,
                    "cta": {"text": "Contact Us", "href": "#contact", "style": "primary"},
                    "style": "transparent-fixed",
                    "scrollBehavior": {"changeOnScroll": True, "scrollThreshold": 100}
                },
                "footer": {
                    "logo": business_name,
                    "tagline": tagline or f"Your trusted {business_type.lower()} partner",
                    "sections": [
                        {"title": "Quick Links", "links": nav_links[:3]},
                        {"title": "Connect", "links": [
                            {"label": "Facebook", "href": "#"},
                            {"label": "Instagram", "href": "#"},
                            {"label": "Twitter", "href": "#"}
                        ]}
                    ],
                    "copyright": f"© {datetime.now().year} {business_name}. All rights reserved."
                }
            },
            "globalStyles": self._get_default_global_styles(
                business_data.get("style_preferences", ["Modern"])
            ),
            "designVision": {
                "design_theme": "modern",
                "hero_concept": "Clean and professional hero with clear call-to-action",
                "visual_personality": "Professional and trustworthy"
            }
        }
    
    def _fix_component_types(self, blueprint: Dict[str, Any]) -> Dict[str, Any]:
        """
        Fix component types to match their IDs.
        
        AI sometimes generates generic types like 'Features' or 'About' 
        for specific features like 'games', 'tournaments', 'community'.
        This ensures the type matches the ID for proper template selection.
        """
        # Mapping of component IDs to their correct types
        ID_TO_TYPE_MAP = {
            # Gaming components
            "games": "Games",
            "tournaments": "Tournaments", 
            "community": "Community",
            # Movie components
            "movies": "Movies",
            "showtimes": "Showtimes",
            "tickets": "Tickets",
            # Restaurant/Cafe components
            "menu": "Menu",
            "our_menu": "Menu",
            "specials": "Specials",
            "today's_specials": "Specials",
            "hours": "Hours",
            "hours_&_location": "Hours",
            "location": "Hours",
            # Common components
            "hero": "Home",
            "home": "Home",
            "about": "About",
            "our_story": "About",
            "gallery": "Gallery",
            "contact": "Contact",
            "testimonials": "Testimonials",
            "customer_love": "Testimonials",
            "faq": "FAQ",
            "cta": "CTA",
            "services": "Services",
            "features": "Features",
            "products": "Products",
            "projects": "Projects",
        }
        
        components = blueprint.get("components", {})
        
        for comp_key, comp_data in components.items():
            comp_id = comp_data.get("id", "").lower()
            current_type = comp_data.get("type", "")
            
            # Check if this ID has a specific type mapping
            if comp_id in ID_TO_TYPE_MAP:
                correct_type = ID_TO_TYPE_MAP[comp_id]
                if current_type != correct_type:
                    print(f"[BlueprintService] 🔄 Fixing {comp_id}: {current_type} → {correct_type}")
                    comp_data["type"] = correct_type
        
        return blueprint

    def _ensure_all_features_present(
        self,
        blueprint: Dict[str, Any],
        features: List[Any],
        business_data: Dict[str, Any],
        metadata: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Ensure all selected features have corresponding components.
        
        AI sometimes skips features in its response. This method adds
        missing components using fallback templates.
        
        Args:
            blueprint: Generated blueprint
            features: List of selected features (names or objects)
            business_data: Business information
            metadata: Full metadata
            
        Returns:
            Blueprint with all features as components
        """
        components = blueprint.get("components", {})
        
        # Extract feature names (handle both string list and object list)
        feature_names = []
        for f in features:
            if isinstance(f, dict):
                feature_names.append(f.get("name", f.get("id", "")))
            else:
                feature_names.append(str(f))
        
        # Normalize feature names for comparison
        def normalize_name(name: str) -> str:
            return name.lower().replace(" ", "_").replace("'", "").replace("&", "and")
        
        # Get existing component IDs
        existing_ids = set()
        for comp_key, comp in components.items():
            comp_id = comp.get("id", comp_key.replace("comp-", ""))
            existing_ids.add(normalize_name(comp_id))
            # Also add the key without prefix
            existing_ids.add(normalize_name(comp_key.replace("comp-", "")))
        
        # Feature name to component type mapping
        FEATURE_TO_TYPE = {
            "hero": "Home",
            "home": "Home",
            "about": "About",
            "our story": "About", 
            "about us": "About",
            "menu": "Menu",
            "our menu": "Menu",
            "specials": "Specials",
            "today's specials": "Specials",
            "daily specials": "Specials",
            "hours": "Hours",
            "hours & location": "Hours",
            "hours and location": "Hours",
            "location": "Hours",
            "gallery": "Gallery",
            "photos": "Gallery",
            "testimonials": "Testimonials",
            "reviews": "Testimonials",
            "customer love": "Testimonials",
            "contact": "Contact",
            "contact us": "Contact",
            "get in touch": "Contact",
            "faq": "FAQ",
            "cta": "CTA",
            "call to action": "CTA",
            "services": "Services",
            "our services": "Services",
            "features": "Features",
            "pricing": "Pricing",
            "team": "Team",
            "our team": "Team",
            "blog": "Blog",
            "reservations": "Contact",  # Map to contact with booking form
            "special offers": "Specials",
        }
        
        # Get business info for fallback components
        business_name = (
            metadata.get("business_name") or 
            business_data.get("business_name") or 
            "Your Business"
        )
        business_type = business_data.get("business_type", "Business")
        services = business_data.get("services", [])
        
        missing_count = 0
        
        for feature_name in feature_names:
            normalized = normalize_name(feature_name)
            
            # Check if this feature already has a component
            if normalized in existing_ids:
                continue
            
            # Also check partial matches
            found = False
            for existing_id in existing_ids:
                if normalized in existing_id or existing_id in normalized:
                    found = True
                    break
            
            if found:
                continue
            
            # Feature is missing - create fallback component
            feature_lower = feature_name.lower()
            comp_type = FEATURE_TO_TYPE.get(feature_lower, "Features")
            comp_id = normalized.replace("_", "-")
            comp_key = f"comp-{comp_id}"
            
            # Create fallback component
            new_component = self._create_fallback_component(
                comp_id=comp_id,
                comp_type=comp_type,
                business_name=business_name,
                business_type=business_type,
                services=services
            )
            
            # Override name with actual feature name
            new_component["name"] = feature_name
            
            components[comp_key] = new_component
            missing_count += 1
            print(f"[BlueprintService] ➕ Added missing component: {feature_name} ({comp_type})")
        
        blueprint["components"] = components
        
        if missing_count > 0:
            print(f"[BlueprintService] ✅ Added {missing_count} missing components from selected features")
        else:
            print(f"[BlueprintService] ✅ All {len(feature_names)} selected features have components")
        
        return blueprint

    def _create_fallback_component(
        self,
        comp_id: str,
        comp_type: str,
        business_name: str,
        business_type: str,
        services: List[str]
    ) -> Dict[str, Any]:
        """
        Create a fallback component with basic content.
        
        Args:
            comp_id: Component ID
            comp_type: Component type
            business_name: Business name
            business_type: Business type
            services: List of services
            
        Returns:
            Component dictionary
        """
        layout_variants = BlueprintPrompts.get_layout_variants()
        variant = random.choice(layout_variants.get(comp_type, ["default"]))
        
        base_animation = {
            "type": "fade-slide-up",
            "duration": 600,
            "stagger": 100,
            "easing": "cubic-bezier(0.25, 1, 0.5, 1)"
        }
        
        if comp_type == "About":
            return {
                "id": comp_id,
                "type": "About",
                "name": "About Section",
                "props": {
                    "layoutVariant": variant,
                    "title": f"About {business_name}",
                    "story": f"Welcome to {business_name}, your trusted partner in {business_type.lower()} excellence. We are committed to delivering outstanding quality and service to every customer.",
                    "stats": [
                        {"value": "100+", "label": "Happy Customers"},
                        {"value": "5+", "label": "Years Experience"},
                        {"value": "50+", "label": "Projects Completed"}
                    ]
                },
                "animation": base_animation
            }
        
        elif comp_type == "Features":
            feature_list = []
            icons = ["✨", "🎯", "💡", "🚀", "⭐", "🎨"]
            default_services = services if services else ["Quality Service", "Expert Team", "24/7 Support", "Best Prices"]
            
            for i, service in enumerate(default_services[:6]):
                feature_list.append({
                    "icon": icons[i % len(icons)],
                    "title": service,
                    "description": f"We provide exceptional {service.lower()} tailored to your needs."
                })
            
            return {
                "id": comp_id,
                "type": "Features",
                "name": "Features Section",
                "props": {
                    "layoutVariant": variant,
                    "sectionTitle": "What We Offer",
                    "sectionSubtitle": f"Discover what makes {business_name} special",
                    "featureList": feature_list
                },
                "animation": base_animation
            }
        
        elif comp_type == "Menu":
            return {
                "id": comp_id,
                "type": "Menu",
                "name": "Menu Section",
                "props": {
                    "layoutVariant": variant,
                    "sectionTitle": "Our Menu",
                    "categories": ["Starters", "Mains", "Desserts"],
                    "items": [
                        {"name": "Signature Dish", "description": "Our chef's special creation", "price": "$15.99", "category": "Mains"},
                        {"name": "Fresh Salad", "description": "Garden fresh vegetables", "price": "$8.99", "category": "Starters"},
                        {"name": "Sweet Delight", "description": "Homemade dessert", "price": "$6.99", "category": "Desserts"}
                    ]
                },
                "animation": base_animation
            }
        
        elif comp_type == "Gallery":
            return {
                "id": comp_id,
                "type": "Gallery",
                "name": "Gallery Section",
                "props": {
                    "layoutVariant": variant,
                    "title": "Our Gallery",
                    "subtitle": f"See what {business_name} has to offer",
                    "categories": ["All", "Featured", "Recent"],
                    "images": [
                        "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4",
                        "https://images.unsplash.com/photo-1555396273-367ea4eb4db5",
                        "https://images.unsplash.com/photo-1414235077428-338989a2e8c0"
                    ]
                },
                "animation": base_animation
            }
        
        elif comp_type == "Testimonials":
            return {
                "id": comp_id,
                "type": "Testimonials",
                "name": "Testimonials Section",
                "props": {
                    "layoutVariant": variant,
                    "sectionTitle": "What Our Customers Say",
                    "testimonials": [
                        {"quote": f"Amazing experience at {business_name}! Highly recommended.", "author": "John D.", "role": "Customer"},
                        {"quote": "Professional service and great quality. Will definitely come back!", "author": "Sarah M.", "role": "Customer"},
                        {"quote": "The best in town! Exceeded all my expectations.", "author": "Mike R.", "role": "Customer"}
                    ]
                },
                "animation": base_animation
            }
        
        elif comp_type == "CTA":
            return {
                "id": comp_id,
                "type": "CTA",
                "name": "CTA Section",
                "props": {
                    "layoutVariant": variant,
                    "title": "Ready to Get Started?",
                    "description": f"Contact {business_name} today and experience the difference.",
                    "ctaText": "Get Started Now"
                },
                "animation": base_animation
            }
        
        elif comp_type == "Contact":
            return {
                "id": comp_id,
                "type": "Contact",
                "name": "Contact Section",
                "props": {
                    "layoutVariant": variant,
                    "title": "Get In Touch",
                    "subtitle": "We'd love to hear from you",
                    "formFields": [
                        {"type": "text", "name": "name", "placeholder": "Your Name", "required": True},
                        {"type": "email", "name": "email", "placeholder": "Email Address", "required": True},
                        {"type": "text", "name": "phone", "placeholder": "Phone Number", "required": False},
                        {"type": "textarea", "name": "message", "placeholder": "Your Message", "required": True, "rows": 4}
                    ],
                    "ctaText": "Send Message"
                },
                "animation": base_animation
            }
        
        # ===== Gaming Website Components =====
        elif comp_type == "Games":
            return {
                "id": comp_id,
                "type": "Games",
                "name": "Games Section",
                "props": {
                    "layoutVariant": variant,
                    "sectionTitle": "Our Games",
                    "sectionSubtitle": "Explore our collection",
                    "games": [
                        {"title": "Action Adventure", "genre": "Action", "rating": "4.8", "description": "Epic journey awaits"},
                        {"title": "Strategy Master", "genre": "Strategy", "rating": "4.5", "description": "Test your tactical skills"},
                        {"title": "Racing Fury", "genre": "Racing", "rating": "4.7", "description": "High-speed excitement"}
                    ]
                },
                "animation": base_animation
            }
        
        elif comp_type == "Tournaments":
            return {
                "id": comp_id,
                "type": "Tournaments",
                "name": "Tournaments Section",
                "props": {
                    "layoutVariant": variant,
                    "sectionTitle": "Tournaments",
                    "sectionSubtitle": "Join the competition",
                    "events": [
                        {"name": "Championship Series", "date": "Coming Soon", "prize": "$10,000", "status": "Registering"},
                        {"name": "Weekly Challenge", "date": "Every Saturday", "prize": "$500", "status": "Open"}
                    ]
                },
                "animation": base_animation
            }
        
        elif comp_type == "Community":
            return {
                "id": comp_id,
                "type": "Community",
                "name": "Community Section",
                "props": {
                    "layoutVariant": variant,
                    "sectionTitle": "Join Our Community",
                    "sectionSubtitle": "Connect with fellow gamers",
                    "platforms": [
                        {"name": "Discord", "members": "10K+", "link": "#"},
                        {"name": "Forums", "members": "5K+", "link": "#"},
                        {"name": "Reddit", "members": "8K+", "link": "#"}
                    ]
                },
                "animation": base_animation
            }
        
        elif comp_type == "FAQ":
            return {
                "id": comp_id,
                "type": "FAQ",
                "name": "FAQ Section",
                "props": {
                    "layoutVariant": variant,
                    "sectionTitle": "Frequently Asked Questions",
                    "faqs": [
                        {"question": "How do I get started?", "answer": "Simply sign up and explore our services."},
                        {"question": "What payment methods do you accept?", "answer": "We accept all major credit cards and PayPal."},
                        {"question": "How can I contact support?", "answer": "Reach out via our contact form or email us directly."}
                    ]
                },
                "animation": base_animation
            }
        
        # ===== Restaurant/Cafe Specific Components =====
        elif comp_type == "Specials":
            return {
                "id": comp_id,
                "type": "Specials",
                "name": "Today's Specials",
                "props": {
                    "layoutVariant": variant,
                    "sectionTitle": "Today's Specials",
                    "items": [
                        {"name": "Chef's Special", "description": "A delightful creation by our head chef", "price": "$15.99", "badge": "Popular"},
                        {"name": "Soup of the Day", "description": "Homemade soup prepared fresh every morning", "price": "$6.99", "badge": "New"},
                        {"name": "Daily Combo", "description": "Main course + drink + dessert", "price": "$19.99", "badge": "Best Value"}
                    ]
                },
                "animation": base_animation
            }
        
        elif comp_type == "Hours":
            return {
                "id": comp_id,
                "type": "Hours",
                "name": "Hours & Location",
                "props": {
                    "layoutVariant": variant,
                    "title": "Hours & Location",
                    "address": "123 Main Street, City, State 12345",
                    "phone": "(555) 123-4567",
                    "email": f"hello@{business_name.lower().replace(' ', '')}.com",
                    "hours": [
                        {"day": "Monday - Friday", "time": "7:00 AM - 9:00 PM"},
                        {"day": "Saturday", "time": "8:00 AM - 10:00 PM"},
                        {"day": "Sunday", "time": "9:00 AM - 8:00 PM"}
                    ]
                },
                "animation": base_animation
            }
        
        elif comp_type == "Services":
            return {
                "id": comp_id,
                "type": "Services",
                "name": "Our Services",
                "props": {
                    "layoutVariant": variant,
                    "sectionTitle": "Our Services",
                    "categories": ["Main Services"],
                    "items": [
                        {"name": "Quality Food", "description": "Fresh ingredients prepared with care", "category": "Main Services"},
                        {"name": "Premium Service", "description": "Exceptional dining experience guaranteed", "category": "Main Services"},
                        {"name": "Fast Delivery", "description": "Quick delivery to your doorstep", "category": "Main Services"}
                    ]
                },
                "animation": base_animation
            }
        
        # ===== Movie Website Components =====
        elif comp_type == "Movies":
            return {
                "id": comp_id,
                "type": "Movies",
                "name": "Now Showing Section",
                "props": {
                    "layoutVariant": variant,
                    "sectionTitle": "Now Showing",
                    "movies": [
                        {"title": "Blockbuster Action", "genre": "Action", "rating": "PG-13", "duration": "2h 30m"},
                        {"title": "Comedy Night", "genre": "Comedy", "rating": "PG", "duration": "1h 45m"},
                        {"title": "Mystery Thriller", "genre": "Thriller", "rating": "R", "duration": "2h 10m"}
                    ]
                },
                "animation": base_animation
            }
        
        elif comp_type == "Showtimes":
            return {
                "id": comp_id,
                "type": "Showtimes",
                "name": "Showtimes Section",
                "props": {
                    "layoutVariant": variant,
                    "sectionTitle": "Showtimes",
                    "dates": ["Today", "Tomorrow", "This Weekend"]
                },
                "animation": base_animation
            }
        
        elif comp_type == "Tickets":
            return {
                "id": comp_id,
                "type": "Tickets",
                "name": "Book Tickets Section",
                "props": {
                    "layoutVariant": variant,
                    "sectionTitle": "Book Tickets",
                    "sectionSubtitle": "Reserve your seats now"
                },
                "animation": base_animation
            }
        
        else:
            # Generic component
            return {
                "id": comp_id,
                "type": comp_type,
                "name": f"{comp_type} Section",
                "props": {
                    "layoutVariant": "default",
                    "title": comp_type,
                    "description": f"Content for {comp_type} section"
                },
                "animation": base_animation
            }


# Singleton instance
_blueprint_service_instance: Optional[BlueprintService] = None


def get_blueprint_service() -> BlueprintService:
    """Get or create BlueprintService singleton instance"""
    global _blueprint_service_instance
    if _blueprint_service_instance is None:
        _blueprint_service_instance = BlueprintService()
    return _blueprint_service_instance
