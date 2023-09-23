<div align="center">

# ThreadShare

</div>

<br>
<div style="text-align: center;">
  <img src="./asset/ThreadShare_logo.png" alt="Your Logo" width="100">
</div>
<br>
<p align="center">
    <strong>A Python library to maximise CPU usage by smartly sharing threads among multiple functions. </strong>
</p>


## Why <span style="color:lightblue;"> ThreadShare </span> ?

Systems with a limited number of cores, like the Raspberry Pi, struggle with CPU resource constraints, making it challenging to efficiently execute multiple tasks functions.

ThreadShare is an Python library designed to efficiently utilize a single CPU core by dynamically sharing threads among multiple functions. It adapts to the execution rates and computational loads of tasks to ensure optimal performance.

## Key Features
- **Thread Loop Sharing**: Run multiple functions at different rates on shared threads.
- **Dynamic Thread Management**: Automatically manages thread creation and load balancing.
**Adaptive Load Balancing**: Dynamically allocate tasks to threads based on their load.
- **Rate-Based Task Scheduling**: Schedules tasks based on their execution rates.
- **Resource Monitoring**: Monitors CPU and memory usage to adaptively manage thread utilization.
- **Graceful Shutdown**: Ensures all tasks are completed before shutting down.

## Installation

To install ThreadShare, you can use pip:

```bash
pip install ThreadShare
```

## Usage

Here is a basic example to demonstrate how to use ThreadShare:

```python
from ThreadShare import ThreadManager

# Define your function
def example_task():
    print("Task executed.")

# Initialize ThreadManager
manager = ThreadManager()

# Add tasks
manager.add_task(example_task, rate=0.2)

# Shutdown (optional)
manager.shutdown()
```

## Metrics and Monitoring

ThreadShare provides real-time metrics and resource monitoring. These metrics can be accessed programmatically for advanced use-cases or can be logged for monitoring and debugging.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
