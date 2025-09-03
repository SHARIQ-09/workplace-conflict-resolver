import os
import json
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Updated Prompt Template with Solution Choices A, B, C
prompt_template = """
You are a workplace conflict resolution expert.
Analyze the following workplace conversation carefully:

1. Identify any signs of potential conflict, misunderstanding, or communication breakdown.
2. Detect negative tones such as frustration, defensiveness, or sarcasm, if present.
3. Suggest 3 constructive and respectful ways (labeled as choices A, B, and C) that both parties can resolve the conflict.

Keep your tone neutral and professional. Your goal is to help improve workplace communication.

Here is the conversation:
---
{conversation}
---

Respond ONLY with a valid JSON object in this format:
{{
  "conflict_risk": "Low/Moderate/High",
  "issues_detected": ["Issue 1", "Issue 2"],
  "resolution_choices": {{
    "A": "First possible solution here",
    "B": "Second possible solution here",
    "C": "Third possible solution here"
  }}
}}
"""

def detect_conflict(conversation: str):
    prompt = prompt_template.format(conversation=conversation)
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a workplace conflict resolution expert."},
            {"role": "user", "content": prompt}
        ],
        model="llama-3.3-70b-versatile",  # You can change model if needed
        temperature=0,
    )

    response_text = chat_completion.choices[0].message.content.strip()

    print("====== MODEL RESPONSE ======")
    print(response_text)
    print("====== END RESPONSE ======")

    try:
        response_json = json.loads(response_text)
    except json.JSONDecodeError:
        raise ValueError("Model response is not valid JSON")
    
    return response_json

