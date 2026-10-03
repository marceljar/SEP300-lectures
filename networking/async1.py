import asyncio

async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay) 
    print(f"{name} finished after {delay} seconds")

async def main():
    task1 = asyncio.create_task(task("Task A", 3))
    task2 = asyncio.create_task(task("Task B", 1))
    task3 = asyncio.create_task(task("Task C", 4))
    task4 = asyncio.create_task(task("Task D", 2))

    await task1
    await task2
    await task3
    await task4

asyncio.run(main())
