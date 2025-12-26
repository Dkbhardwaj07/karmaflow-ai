import time
from gemini_client import call_gemini

LAST_CALL = 0
MIN_INTERVAL = 15  # seconds (safe for free tier)

def verify(task, result):
    global LAST_CALL

    # 🚦 throttle Gemini calls
    now = time.time()
    if now - LAST_CALL < MIN_INTERVAL:
        print("⏳ Skipping Gemini verify (rate limit protection)")
        return result["status"] == "success"

    LAST_CALL = now

    prompt = f"""
You are a strict verification agent.

TASK:
{task["task"]}

SUCCESS CRITERIA:
{task["success"]}

EXECUTION OUTPUT:
{result}

Answer ONLY:
PASS or FAIL
"""

    verdict = call_gemini(prompt, temperature=0)
    return verdict.strip().startswith("PASS")
