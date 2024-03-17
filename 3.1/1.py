from time import sleep, perf_counter
import asyncio

# Последовательное выполнение функций-корутин

# async def coro(num, seconds):
#     print(f"coro{num} начала свое выполнение")
#     await asyncio.sleep(seconds)
#     print(f"coro{num} выполнена за {seconds} секунд(ы)")


# async def main():
#     coro1 = coro(1, 3)
#     coro2 = coro(2, 1)
#     await coro2
#     await coro1

# start = perf_counter()
# asyncio.run(main())
# print(f"Программа выполнена за {perf_counter() - start:.3f} секунд(ы)")


# Асинхронное выполнение функций-корутин

async def coro(num, seconds):
    print(f"coro{num} начала свое выполнение")
    await asyncio.sleep(seconds)
    print(f"coro{num} выполнена за {seconds} секунд(ы)")


async def main():
    task1 = asyncio.create_task(coro(1, 3))
    task2 = asyncio.create_task(coro(2, 1))
    await task2
    await task1

start = perf_counter()
asyncio.run(main())
print(f"Программа выполнена за {perf_counter() - start:.3f} секунд(ы)")
