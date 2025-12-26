# We store:goal, current day, completed tasks, failed attempts, decisions made by agent
import json
from datetime import datetime
import os

class AgentMemory:
    def __init__(self, path="state.json"):
        self.path = path
        self.state = self.load()

    def load(self):
        # File exist nahi karti
        if not os.path.exists(self.path):
            return self._empty_state()

        # File empty hai
        if os.path.getsize(self.path) == 0:
            return self._empty_state()

        try:
            with open(self.path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return self._empty_state()

    def _empty_state(self):
        return {
            "goal": "",
            "current_task": None,
            "completed_tasks": [],
            "failed_tasks": [],
            "thought_log": [],
            "last_updated": None
        }

    def save(self):
        self.state["last_updated"] = datetime.utcnow().isoformat()
        with open(self.path, "w") as f:
            json.dump(self.state, f, indent=2)

    def log_thought(self, thought):
        self.state["thought_log"].append(thought)
        self.save()
