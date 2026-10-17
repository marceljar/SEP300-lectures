import asyncio

async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay) 
    print(f"{name} finished after {delay} seconds")

async def main():
    await asyncio.gather(
        task("Task A", 3),
        task("Task B", 1),
        task("Task C", 4),
        task("Task D", 2),
    )

asyncio.run(main())
