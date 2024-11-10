# High score tracker with file persistence
import json
import os

SCORES_FILE = "scores.json"


class HighScore:
    def __init__(self):
        self.entries = self.load()

    def add(self, name, score, time_secs):
        self.entries.append({"name": name, "score": score, "time": time_secs})
        self.entries.sort(key=lambda e: e["score"], reverse=True)
        self.save()

    def top(self, n=10):
        return self.entries[:n]

    def save(self):
        with open(SCORES_FILE, "w") as f:
            json.dump(self.entries[:10], f)

    def load(self):
        if os.path.exists(SCORES_FILE):
            try:
                with open(SCORES_FILE) as f:
                    return json.load(f)
            except (json.JSONDecodeError, KeyError):
                pass
        return []
