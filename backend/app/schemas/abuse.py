from pydantic import BaseModel

class AbuseRequest(BaseModel):
    conversation: str

class AbuseResponse(BaseModel):
    abuse_detected: bool
    types: list[str]
    severity_score: int
    explanation: str
