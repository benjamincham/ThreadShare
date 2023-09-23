
import threading
import logging
import time
import psutil

logging.basicConfig(level=logging.INFO)

class Monitor:
    def __init__(self, manager):
        self.manager = manager
        self.shutdown_event = manager.shutdown_event

    def start(self):
        while not self.shutdown_event.is_set():
            cpu_usage = psutil.cpu_percent()
            memory_info = psutil.virtual_memory()
            logging.info(f"Resource Metrics: CPU Usage {cpu_usage}%, Memory Usage {memory_info.percent}%")

            for t in self.manager.threads:
                logging.info(f"Thread Metrics: Thread {t['thread'].name}, Executed Tasks {t['thread'].executed_tasks}")
            time.sleep(2)
        