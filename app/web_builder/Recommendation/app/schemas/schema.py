from pydantic import BaseModel
from typing import Dict, List, Optional

class StartRequest(BaseModel):
    prompt: str
    language: str

class NextQuestionRequest(BaseModel):
    session_id: str
    question_id: str
    answer: str

class PaletteRequest(BaseModel):
    session_id: str

class SelectPaletteRequest(BaseModel):
    session_id: str
    palette_id: str

class FeatureRequest(BaseModel):
    session_id: str

class SelectFeaturesRequest(BaseModel):
    session_id: str
    selected_features: List[str]

class FinalizeRequest(BaseModel):
    session_id: str
    project_id: int
    selected_features: Optional[List[str]] = None
    selectedFeatures: Optional[List[str]] = None
    feature_ids: Optional[List[str]] = None
    features: Optional[List[str]] = None


class UpdateAnswerRequest(BaseModel):
    session_id: str
    question_id: str
    new_answer: str