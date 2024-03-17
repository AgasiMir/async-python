from time import sleep, perf_counter
from random import randint
import asyncio


async def boil_water(time: int):
    print('Ставим чайник с водой на плиту')
    await asyncio.sleep(time)
    print("Чайник закипел!")


async def chop_vedgetables():
    print('Начинаем нарезку овощей...')
    await asyncio.sleep(randint(2, 4))
    print("Овощи готовы")


async def prepare_dinner():

    #----вариант 1: короткий----

    # await asyncio.gather(boil_water(5), chop_vedgetables())

     #----вариант 2: длинный----

    task1 = asyncio.create_task(boil_water(5))
    task2 = asyncio.create_task(chop_vedgetables())

    await task1
    await task2


asyncio.run(prepare_dinner())
