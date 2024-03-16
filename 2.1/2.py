import asyncio
from time import perf_counter, sleep


start = perf_counter()

async def sleeping(n):
    print(f"Начало длительной операции № {n}: {perf_counter() - start:.4f}")
    await asyncio.sleep(3)
    print(f"Завершение длительной операции {n}")


async def main():
    task = [sleeping(i) for i in range(1, 31)]
    tasks = await asyncio.gather(*task)
    print(f"Выполненно операций: {len(tasks)}")
    print(f"Программа завершена за секунд: {perf_counter() - start:.4f}")


asyncio.run(main())
