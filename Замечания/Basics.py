"""
Как работает, как мне кажется асинхронность. К таким выводам я пришел к концу 3 главы
курса Асинхронный Python.

Вся асинхронность приходит в движение с подачи ключевого слова await. Будь то asyncio.sleep(x),
запуск корутинных функций и т.д. То есть само по себе существование функции-корутины async def
еще не значит, что данная функция будет работать асинхронно.

Ключевое слово await дает сигнал на переключение контекста. Пример из жизни: поставил
чайник кипятиться, делегировал данную задачу газовой плите, и оператор await переключил
контекст, то есть, разрешил мне заняться другими делами, например, приготовить бутерброды,
ожидая ответ от чайника. Как только вода в чайник вскипятиться, чайник начнет свистеть,
подавая тем самым сигнал о завершении функции-корутины "поставить чайник".
Тогда await снова переключит контекст, и я займусь чаем.

Кроме всего вышеперечисленного, чтобы функция работала асинхронно, нужно создать объект
класса Task, передав в качестве аргумента данную функцию-корутину. И уже сам объект вызвать
посредством оператора await. Если просто записать await функция-корутина(), то это, хоть и
вызовет функция, но все будет происходить в синхронном режиме.

Примеры:
"""

import asyncio
import time


async def поставить_чайник(num: int):
    await asyncio.sleep(num)
    print("Вода закипела")


async def сделать_бутерброды(num: int):
    await asyncio.sleep(num)
    print("Бутерброды готовы")


async def sync_main():
    await поставить_чайник(4)
    await сделать_бутерброды(3)


async def Async_main():

    """1 вариант"""

    # task_1 = asyncio.create_task(поставить_чайник(4))
    # task_2 = asyncio.create_task(сделать_бутерброды(3))

    # await task_1
    # await task_2

    """2 вариант"""

    # tasks = [asyncio.create_task(поставить_чайник(4)), asyncio.create_task(сделать_бутерброды(3))]
    # for task in tasks:
    #     await task

    """3 вариант. При использовании метода gather, можно обоойтись без asyncio.create_task"""

    tasks = [поставить_чайник(4), сделать_бутерброды(3)]
    await asyncio.gather(*tasks)


start = time.time()
# asyncio.run(sync_main())
asyncio.run(Async_main())
print(f"Все задачи завершились за {time.time() - start:.4f} с.")


"""
В случае с sync_main() мы хоть и запускаем функции-корутины оператором await,
но работают они синхронно, и я жду, пока закипит вода, и только после этого делаю
бутерброды. Всё вместе это занимает чуть больше 7 секунд. При этом в консоли сначала выводится
'Вода закипела', а потом 'Бутерброды готовы'.

И совсем другое дело, когда мы функции-корутины оборачиваем в экземпляры класса Task.
Запустив точку входа Async_main(), можно увидеть, что, во первых, сначала выводится
'Бутерброды готовы', так как это занимает 3 секунды, а уже потом 'Вода закипела',
так как чайнику потребовалось на это 4 секунды, хотя сначала вызывается именно что
функция 'поставить_чайник'. Кроме того, и это во вторых, в общем и целом, приготовление
завтрака чай + бутеры заняло 4 секунды, точнее 4 секунды с небольшим, так как переключение
контекста тоже требует немного времени. То есть все вместе заняло почти столько времени,
сколько требуется на самое длительное по времени действие, в данном случае - это вскипятить воду.

"""
