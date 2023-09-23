
import threading
import logging
from queue import Queue
import psutil
from threading import Event
from .task import Task
from .managed_thread import ManagedThread

logging.basicConfig(level=logging.INFO)

class ThreadManager:
    def __init__(self):
        self.threads = []
        self.shutdown_event = Event()
        self.create_thread()

    def create_thread(self):
        task_queue = Queue()
        thread = ManagedThread(task_queue, self.shutdown_event)
        thread.start()
        self.threads.append({'thread': thread, 'queue': task_queue})

    def add_task(self, func, rate_ms):
        task = Task(func, rate_ms)
        min_load_thread = min(self.threads, key=lambda x: x['thread'].load)

        cpu_usage = max(psutil.cpu_percent(percpu=True))
        if min_load_thread['thread'].load + rate_ms >500 or cpu_usage > 70:
            self.create_thread()
            min_load_thread = self.threads[-1]

        min_load_thread['thread'].load += rate_ms
        min_load_thread['queue'].put(task)
        logging.info(f"Task added to thread {min_load_thread['thread'].name} with load {min_load_thread['thread'].load}")

    def shutdown(self):
        logging.info("Initiating graceful shutdown...")
        self.shutdown_event.set()
        for t in self.threads:
            t['thread'].join()
        