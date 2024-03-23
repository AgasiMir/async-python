import asyncio

# Список поваров.
сhef_list = ['', 'Франсуа', 'Жан', 'Марсель']


async def cook_order(order_number, dish):
    # Повар готовит блюдо
    print(f"Повар {сhef_list[order_number]} начинает готовить заказ №{order_number}: {dish}")
    await asyncio.sleep(2)  # Имитация времени на готовку
    print(f"Заказ №{order_number}: {dish} готов!")
    return f"{dish} для заказа №{order_number}"


async def serve_order(order_number, dish):
    # Официант подает блюдо
    cooked_dish = await cook_order(order_number, dish)
    print(f"Официант подает {cooked_dish}")


async def manager():
    # Менеджер (событийный цикл) назначает задачи
    orders = [(1, 'Салат'), (2, 'Стейк'), (3, 'Суп')]
    tasks = [asyncio.create_task(serve_order(order_number, dish)) for order_number, dish in orders]

    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks)


# Запуск событийного цикла
asyncio.run(manager())
