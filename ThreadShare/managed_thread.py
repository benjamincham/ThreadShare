
import threading
from queue import Queue, Empty
import time

class ManagedThread(threading.Thread):
    def __init__(self, task_queue, shutdown_event):
        super().__init__()
        self.task_queue = task_queue
        self.load = 0
        self.shutdown_event = shutdown_event
        self.executed_tasks = 0

    def run(self):
        while not self.shutdown_event.is_set():
            try:
                task = self.task_queue.get_nowait()
            except Empty:
                time.sleep(0.1)
                continue
            current_time_ms = round(time.time()*1000)
            if current_time_ms >= task.next_run_time:
                task.func()
                task.next_run_time = current_time_ms + task.rate_ms
                self.executed_tasks += 1
            
            self.task_queue.put(task)
        