import asyncio
from time import sleep


async def fetch_data():
    print("Загрузка данных...")
    await asyncio.sleep(8)
    return "Данные"


async def process_data():
    print("Обработка данных...")
    await asyncio.sleep(1)
    return "Данные обработаны"


async def main():
    fetched_data = await fetch_data()
    processed_data = await process_data()
    print(fetched_data, processed_data)

asyncio.run(main())
