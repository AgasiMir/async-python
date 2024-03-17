from time import sleep, perf_counter
from random import randint
import asyncio


class Pizzeria:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name: str) -> None:
        self.name = name

    async def make_pizza(self, order_id: int) -> None:
        cook_time = randint(2, 5)
        print(f"Пиццерия '{self.name}'начала готовить пиццу для заказа № {order_id:02}")
        await asyncio.sleep(cook_time)
        print(f"Пиццерия '{self.name}' закончила готовить пиццу для заказа № {order_id:02}")


async def main():
    pizzeria = Pizzeria(name="Тесто и Сыр")
    tasks = [pizzeria.make_pizza(i) for i in range(1, 6)]
    await asyncio.gather(*tasks)


start = perf_counter()

asyncio.run(main())

print(f"Все заказы выполнены за {perf_counter() - start}")
