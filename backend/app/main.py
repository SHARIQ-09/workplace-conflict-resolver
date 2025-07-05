from fastapi import FastAPI, HTTPException ,APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.schemas.abuse import AbuseRequest, AbuseResponse
from app.models.abuse_detector import detect_abuse
import json
import os

app = FastAPI()

def clean_json_response(response: str) -> str:
    # Remove Markdown-style code fences (```json ... ```)
    response = response.strip()
    if response.startswith("```json"):
        response = response[7:].strip()
    elif response.startswith("```"):
        response = response[3:].strip()
    if response.endswith("```"):
        response = response[:-3].strip()
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a separate API router under /api
api_router = APIRouter()

@api_router.get("/")
def root():
    return {"message": "Abuse Detection API is running."}




@api_router.post("/detect-abuse", response_model=AbuseResponse)
def detect_abuse_endpoint(request: AbuseRequest):
    try:
        result = detect_abuse(request.conversation)
        cleaned_result = clean_json_response(result)
        parsed_result = json.loads(cleaned_result)
        return AbuseResponse(**parsed_result) 
    except Exception as e:
        import traceback
        print("❌ Internal Error:", str(e))
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
    
# ✅ Include API router at /api
app.include_router(api_router, prefix="/api")

# Correct relative path from backend/app/main.py to frontend/dist:
dist_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend/dist'))
# ✅ Mount the Frontend (this serves your built React app)
app.mount("/", StaticFiles(directory=dist_path, html=True), name="static")

