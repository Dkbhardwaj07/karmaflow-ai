import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ OFFICIAL GEMINI 3 MODEL (AVAILABLE IN YOUR ACCOUNT)
MODEL = "models/gemini-3-flash-preview"

def call_gemini(prompt, temperature=0.3):
    model = genai.GenerativeModel(MODEL)
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": temperature,
            "top_p": 0.9
        }
    )
    return response.text
