from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.schemas.conflict import ConflictRequest, ConflictResolutionResponse
from app.models.conflict_detector import detect_conflict

import json
import os

app = FastAPI()


def clean_json_response(response):
    if isinstance(response, dict):
        return response  # Already a dict; no cleaning needed
    response = response.strip()
    if response.startswith("```json"):
        response = response[7:].strip()
    elif response.startswith("```"):
        response = response[3:].strip()
    if response.endswith("```"):
        response = response[:-3].strip()
    return response


# ✅ Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development only; tighten in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Create API router
api_router = APIRouter()

@api_router.get("/")
def root():
    return {"message": "Conflict resolution API is running."}

@api_router.post("/detect-conflict", response_model=ConflictResolutionResponse)
def detect_conflict_endpoint(request: ConflictRequest):
    """
    Handles conflict detection requests.
    """
    try:
        result = detect_conflict(request.conversation)
        print("=== RAW Model Result ===")
        print(repr(result))
        print("=== END ===")

        if isinstance(result, dict):
            parsed_result = result
        elif isinstance(result, str):
            cleaned_result = clean_json_response(result)
            print("=== CLEANED Result ===")
            print(repr(cleaned_result))
            parsed_result = json.loads(cleaned_result)
        else:
            raise ValueError(f"Unexpected result type: {type(result)}")

        # ✅ Inject default resolution choices (this ensures A, B, C are always there)
        parsed_result["resolution_choices"] = {
            "a": "Hold a private meeting with the involved parties.",
            "b": "Offer mediation through HR.",
            "c": "Set clear communication guidelines for future discussions."
        }

        print("=== PARSED Result ===")
        print(parsed_result)

        return ConflictResolutionResponse(**parsed_result)

    except Exception as e:
        import traceback
        print("❌ Internal Error:", str(e))
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Internal Server Error during conflict detection.")


from fastapi import Body

@api_router.post("/generate-email")
def generate_email_draft(request: dict = Body(...)):
    """
    Generate a professional email draft based on conflict analysis.
    """
    try:
        issues_detected = request.get("issues_detected", [])
        resolution_choices = request.get("resolution_choices", {})

        email_template = f"""
        Subject: Follow-up on Workplace Conflict Discussion

        Hi Team,

        Based on the recent discussion, here is a summary of the identified issues:
        {chr(10).join(f"- {issue}" for issue in issues_detected)}

        Suggested Resolution Options:
        A. {resolution_choices.get('a', 'N/A')}
        B. {resolution_choices.get('b', 'N/A')}
        C. {resolution_choices.get('c', 'N/A')}

        Please let me know your thoughts or if you'd like to schedule a follow-up meeting.

        Best regards,
        [Your Name]
        """
        return {"email_draft": email_template.strip()}
    
    except Exception as e:
        import traceback
        print("❌ Email Generation Error:", str(e))
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Email draft generation failed: {str(e)}")




# ✅ Register the API routes under `/api`
app.include_router(api_router, prefix="/api")

# ✅ Serve Frontend
dist_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend/dist'))
app.mount("/", StaticFiles(directory=dist_path, html=True), name="static")
