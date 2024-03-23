from time import sleep
import asyncio


async def task_func(duration):
    name = asyncio.current_task().get_name()
    print(f"Задача {name} запущена, будет выполнена через {duration}с.")
    await asyncio.sleep(duration)
    print(f"Задача {name} завершена")


async def exeptor(duration):
    # Перехватываем исключение в опасном месте
    try:
        await asyncio.sleep(duration)
        # Здесь возникает исключение
        print(f"Задача {asyncio.current_task().get_name()} вызвала ошибку через {duration}c.")
        raise Exception("Произошла ошибка")
    except Exception as e:
        print(f'При выполнении задачи {asyncio.current_task().get_name()} было поднято исключение: {e}')


async def main():
    task1 = asyncio.create_task(task_func(3), name='first')
    task2 = asyncio.create_task(task_func(1), name='second')
    task3 = asyncio.create_task(exeptor(2), name='exception')
    # Асинхронно запускаем все задачи и ждем результат их выполнения
    await asyncio.gather(task1, task2, task3)


asyncio.run(main())


# В таком случае мы просто получим сообщение об обработанной ошибке,
# а остальные корутины успешно завершат свою работу.
# Такой подход может уберечь ваш код от непредвиденных ошибок из запущенных крутин.
 