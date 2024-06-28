"""
asyncio is ideal for I/O-bound tasks, such as handling network requests, reading and writing files, and working with databases. It allows multiple tasks to run concurrently within a single thread, which is efficient for I/O-bound operations.
Processes are ideal for CPU-bound tasks because they can run in parallel on multiple CPU cores without being limited by the GIL.
Threads are suitable for I/O-bound tasks but can also be used for CPU-bound tasks. However, due to the Global Interpreter Lock (GIL) in CPython, threads are not the best choice for CPU-bound tasks in Python, as only one thread can execute Python bytecode at a time.
"""
import multiprocessing
def print_numbers():
    for i in range(5):
        print(i)

process = multiprocessing.Process(target=print_numbers)
process.start()
process.join()


import threading
def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()


import asyncio

class AsyncContextManager:
    async def __aenter__(self):
        print("Entering context manager")
        return self
    async def __aexit__(self, exc_type, exc_value, traceback):
        print("Exiting context manager")
        return False

async def main():
    async with AsyncContextManager():
        print("Inside context manager")

asyncio.run(main())




async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def main():
    print("Starting")
    await say_hello()
    print("Finished")

# Run the main coroutine
asyncio.run(main())

# Output:
# Starting
# Hello
# (pause for 1 second)
# World
# Finished



async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)
    print("Data fetched")

async def process_data():
    print("Processing data...")
    await asyncio.sleep(1)
    print("Data processed")

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(process_data())

    await task1
    await task2

asyncio.run(main())

# Output:
# Fetching data...
# Processing data...
# (pause for 1 second)
# Data processed
# (pause for 1 second)
# Data fetched

