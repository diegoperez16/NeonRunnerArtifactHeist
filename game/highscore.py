# High score tracker - work in progress

class HighScore:
    def __init__(self):
        self.entries = []

    def add(self, name, score, time_secs):
        self.entries.append({"name": name, "score": score, "time": time_secs})
        self.entries.sort(key=lambda e: e["score"], reverse=True)

    def top(self, n=10):
        return self.entries[:n]
