from time import sleep
import asyncio

bank_account = 1000


async def withdraw_money(amount, lock):
    global bank_account

    async with lock:
        print(f"Сейчас на счету {bank_account}р")
        if bank_account >= amount:
            print(f"Снятие {amount}р успешно")
            await asyncio.sleep(1)

            bank_account -= amount
        else:
            print('На счету недостаточно средств')


async def main():
    lock = asyncio.Lock()
    task1 = asyncio.create_task(withdraw_money(900, lock))
    task2 = asyncio.create_task(withdraw_money(900, lock))

    await asyncio.gather(task1, task2)
    print()
    print(f"Остаток средств {bank_account}р")


asyncio.run(main())


# Пример кода, решающий проблему Race Condition с использованием asyncio.Lock()

# import asyncio

# bank_account = 1000

# lock = asyncio.Lock()

# async def withdraw_money(amount):
# Не работает в таком виде. Вызывает ошибку:

# RuntimeError: Task <Task pending name='Task-3' coro=<withdraw_money() running at my_file:9>
# cb=[_gather.<locals>._done_callback() at
# C:\Users\MyName\AppData\Local\Programs\Python\Python39\lib\asyncio\tasks.py:767]>
# got Future <Future pending> attached to a different loop

# Если lock передавать в функцию из main() - тогда работает.

# UPD: Выяснилось, что ошибка происходит в версии Python 3.9,
# которая установлена у меня. В версии 3.11 ошибки не возникает. Пользуйтесь новыми версиями ))
