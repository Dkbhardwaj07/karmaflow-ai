def execute_task(task):
    print(f"🔧 Executing: {task['task']}")

    # 🎭 demo simulation logic
    if "scrape" in task["task"].lower():
        return {"status": "success", "output": "15 job URLs collected"}

    if "rank" in task["task"].lower():
        return {"status": "success", "output": "5 resumes generated"}

    if "automate" in task["task"].lower():
        return {"status": "success", "output": "5 applications submitted"}

    return {"status": "success", "output": "Task executed"}
