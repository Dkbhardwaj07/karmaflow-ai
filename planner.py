# Gemini 3 will:
# decompose goal
# assign days
# define success criteria per task



from gemini_client import call_gemini
import json

def create_plan(goal):
    prompt = f"""
                You are an autonomous marathon planning agent.

                GOAL:
                {goal}

                Break this into a multi-day execution plan.
                Rules:
                - Tasks must be actionable
                - Each task must have a clear success criterion
                - Tasks should be sequential
                - Assume no human intervention

                Return ONLY valid JSON in this format:
                [
                {{
                    "day": 1,
                    "task": "...",
                    "success": "..."
                }}
                ]
                """
    response = call_gemini(prompt)
    return json.loads(response)

