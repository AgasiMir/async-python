from time import sleep
import asyncio


# Словарь бегунов: Имя + скорость бега (м/с)
# Полный список бегунов скрыт под капотом задачи.
runners = {
    "Молния Марк": 12.8,
    "Ветренный Виктор": 13.5,
    "Скоростной Степан": 11.2,
    "Быстрая Белла": 10.8,
}


async def run_lap(name, speed):
    time_needed = round(100 / speed, 2)
    await asyncio.sleep(time_needed)
    print(f"{name} завершил круг за {time_needed} секунд")


async def main(max_time=10):  # Максимальное время для завершения круга 10 сек
    task = [asyncio.create_task(run_lap(n, s)) for n, s in runners.items()]
    try:
        await asyncio.wait_for(asyncio.gather(*task), timeout=max_time)
    except asyncio.TimeoutError:
        pass


asyncio.run(main())
