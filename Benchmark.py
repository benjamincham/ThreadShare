
# Import required modules for benchmarking
import threading
import time
from multiprocessing.pool import ThreadPool
import matplotlib.pyplot as plt
import numpy as np
from queue import Queue

from ThreadShare.thread_manager import ThreadManager

# Run benchmarks for different numbers of workers
threadshare_times = []
threadpool_times = []

# Thread-safe queue to store results
threadpool_result_queue = Queue()
threadshare_result_queue = Queue()

# Define CPU-bound task function to calculate Fibonacci numbers
def compute_fibonacci(n=20):
    if n <= 1:
        return n
    else:
        return compute_fibonacci(n-1) + compute_fibonacci(n-2)

# Modified compute_fibonacci function to insert results into the queue
def compute_fibonacci_threadpool(n=20):
    result = compute_fibonacci(n)
    threadpool_result_queue.put(result)

    if threadpool_result_queue.qsize() >= task_count:
        pool.close()

# ThreadPool-based implementation
def benchmark_threadpool(task_count, workers):
    global pool  # Declare pool as global to access it inside compute_fibonacci_modified
    pool = ThreadPool(workers)
    
    start_time = time.time()
    pool.map(compute_fibonacci_threadpool, [20] * task_count)
    pool.join()
    end_time = time.time()
    
    threadpool_times.append(end_time - start_time)
    
# Modified compute_fibonacci function to insert results into the queue
def compute_fibonacci_threadshare(n=20):
    result = compute_fibonacci(n)
    threadshare_result_queue.put(result)
   

# benchmark_threadshare function
def benchmark_threadshare(task_count, workers):
    global manager  # Declare manager as global to access it inside compute_fibonacci_threadshare
    global threadshare_end_time
    global threadshare_start_time
    manager = ThreadManager()
    threadshare_start_time = time.time()
    for _ in range(workers):
        manager.add_task(compute_fibonacci_threadshare, 1)  # Adding tasks with zero rate as it's a one-time task

    
    while not manager.shutdown_event.is_set():
        if threadshare_result_queue.qsize() >= task_count:
            threadshare_end_time = time.time()
            manager.shutdown()
            threadshare_times.append(threadshare_end_time-threadshare_start_time)
    
# Number of tasks to run is fixed at 1000
task_count = 1000

# Number of workers to use in the benchmark
worker_counts = [20, 50, 100]


for workers in worker_counts:
    #reset queue
    threadshare_result_queue = Queue()
    threadpool_result_queue = Queue()
    benchmark_threadshare(task_count, workers)
    benchmark_threadpool(task_count, workers)



# Draw and display the diagram
plt.figure(figsize=(10, 6))

# Create horizontal bars
plt.barh(np.arange(len(worker_counts)) - 0.2, threadshare_times, 0.4, label='ThreadShare', color='b')
plt.barh(np.arange(len(worker_counts)) + 0.2, threadpool_times, 0.4, label='ThreadPool', color='r')

# Add text labels at the end of each bar
for i, v in enumerate(threadshare_times):
    plt.text(v + 0.05, i - 0.2, str(round(v, 2)), color='b', va='center', fontweight='bold')
    
for i, v in enumerate(threadpool_times):
    plt.text(v + 0.05, i + 0.2, str(round(v, 2)), color='r', va='center', fontweight='bold')

# Update tick labels and axes labels
plt.yticks(np.arange(len(worker_counts)), [str(wc) for wc in worker_counts])
plt.ylabel('Number of Workers')
plt.xlabel('Total Time (seconds) to perform 1000 compute requests')

# Add title and legend
plt.title('Performance Benchmark: ThreadShare vs ThreadPool')
plt.legend()
plt.tight_layout()

# Show and save the plot
plt.show()
plt.savefig('benchmark_2.png')