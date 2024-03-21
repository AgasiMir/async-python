from time import sleep
import asyncio


# Эмуляция комнаты с замком
class Room:
    def __init__(self) -> None:
        self.lock = asyncio.Lock()

    async def use_(self, name):
        # Захват мьютекса
        await self.lock.acquire()
        try:
            print(f"{name} вошел в комнату")
            # Имитация выполнения работы внутри комнаты
            await asyncio.sleep(1)
            print(f"{name} вышел из комнаты")
        finally:
            # Освобождение мьютекса
            self.lock.release()

    async def use(self, name):
        # Использование менеджера контекста для работы с замком
        async with self.lock:
            print(f"{name} вошел в комнату")
            # Имитация выполнения работы внутри комнаты
            await asyncio.sleep(4)
            print(f"{name} вышел из комнаты")


async def person(name, room):
    # Человек (задача) пытается использовать комнату
    print(f"{name} хочет войти в комнату")
    await room.use(name)


async def main():
    room = Room()  # Инициализация комнаты с замком

    # Создание задач для нескольких людей, пытающихся войти в комнату
    await asyncio.gather(
        person("Алексей", room),
        person("Михаил", room),
        person("Иван", room),
    )


asyncio.run(main())


# В этом исправленном коде async with self.lock: заменяет прямое
# использование await self.lock.acquire() и self.lock.release(),
# обеспечивая автоматическое управление блокировкой.
# Это делает код более безопасным и упрощает его понимание,
# поскольку не требуется явно вызывать методы захвата и освобождения замка,
# минимизируя риск ошибок управления состоянием замка.
