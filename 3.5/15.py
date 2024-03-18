import asyncio
from time import sleep


async def counter(name):
    counters = {"Counter 1": 0, "Counter 2": 0, "Counter 3": 0}
    max_counts = {"Counter 1": 10, "Counter 2": 5, "Counter 3": 15}
    delays = {"Counter 1": 1, "Counter 2": 2, "Counter 3": 0.5}

    for _ in range(15):
        if counters[name] < max_counts[name]:
            counters[name] += 1
            await asyncio.sleep(delays[name])
            print(f"{name}: {counters[name]}")


async def main():
    task1 = asyncio.create_task(counter("Counter 1"))
    task2 = asyncio.create_task(counter("Counter 2"))
    task3 = asyncio.create_task(counter("Counter 3"))

    await task1
    await task2
    await task3


asyncio.run(main())
