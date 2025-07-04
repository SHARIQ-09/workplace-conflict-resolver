import os
from groq import Groq
from dotenv import load_dotenv

# Load .env
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

prompt_template = """
You are a workplace abuse detection assistant.

Analyze the following conversation:
\"\"\"{conversation}\"\"\"

Detect any form of workplace abuse including:
- Threats / Intimidation
- Public Shaming
- Discrimination
- Harassment
- Micromanagement
- Passive Aggression
- Gaslighting
- Any other abusive behavior

⚠️ IMPORTANT:
- Detect all levels of abuse — from severe to mild.
- If there is NO abuse, say so clearly.

Return JSON ONLY:
{{
  "abuse_detected": true or false,
  "types": [list of abuse types],
  "severity_score": integer from 0 to 10,
  "explanation": "..."
}}
"""

def detect_abuse(conversation: str):
    prompt = prompt_template.format(conversation=conversation)
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an impartial workplace abuse detection assistant."},
            {"role": "user", "content": prompt}
        ],
        model="llama3-70b-8192",  # Adjust model as needed
        temperature=0,
    )

    response = chat_completion.choices[0].message.content.strip()
    print("====== MODEL RESPONSE ======")
    print(response)
    print("====== END RESPONSE ======")
    return response
