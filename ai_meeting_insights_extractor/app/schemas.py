from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class Options(BaseModel):
    model_name: str = Field(default="google/flan-t5-base")
    max_chunk_chars: int = Field(default=4000)
    summary_bullets: int = Field(default=5)

class InsightsRequest(BaseModel):
    transcript: str
    options: Optional[Options] = None

class SummarizeRequest(BaseModel):
    transcript: str
    options: Optional[Options] = None

class ExtractRequest(BaseModel):
    transcript: str

class ActionItem(BaseModel):
    speaker: Optional[str] = None
    item: str
    due: Optional[str] = None

class InsightsResponse(BaseModel):
    summary: List[str]
    action_items: List[ActionItem]
    meta: Dict[str, Any] = {}
