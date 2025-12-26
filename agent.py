from planner import create_plan
from executor import execute_task
from verifier import verify
from memory import AgentMemory

MAX_RETRIES = 3

def run_agent(goal):
    memory = AgentMemory()
    memory.state["goal"] = goal

    print("🧠 Creating plan...")
    plan = create_plan(goal)
    print("📅 Plan generated:", plan)

    for task in plan:
        attempts = 0
        success = False

        while attempts < MAX_RETRIES and not success:
            attempts += 1
            print(f"\n🔁 Attempt {attempts} | {task['task']}")
            memory.log_thought(f"Attempt {attempts} for {task['task']}")

            result = execute_task(task)
            success = verify(task, result)

            if not success:
                print("❌ Verification failed. Retrying...")
                memory.log_thought("Verification failed")

        if success:
            print("✅ Task completed")
            memory.state["completed_tasks"].append(task)
        else:
            print("🚫 Task failed after retries")
            memory.state["failed_tasks"].append(task)

        memory.save()

if __name__ == "__main__":
    run_agent("Find and apply to 5 Python backend jobs in 3 days")
