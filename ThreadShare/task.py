
class Task:
    def __init__(self, func, rate_ms):
        self.func = func
        self.rate_ms = rate_ms
        self.next_run_time = 0
        