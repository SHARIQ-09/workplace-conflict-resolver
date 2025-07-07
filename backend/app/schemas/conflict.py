from pydantic import BaseModel
from typing import List, Dict

class ConflictRequest(BaseModel):
    conversation: str

class ConflictResolutionResponse(BaseModel):
    conflict_risk: str
    issues_detected: List[str]
    resolution_choices: Dict[str, str]
