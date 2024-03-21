from time import sleep
import asyncio


bank_account = 1000

async def withdraw_money(amount):
    global bank_account
    if bank_account >= amount:
        print(f"Снятие {amount}р успешно")
        await asyncio.sleep(1)

        # Вычитание суммы снятия из общего банковского счета  
        bank_account -= amount

async def main():
    task1 = asyncio.create_task(withdraw_money(900))
    task2 = asyncio.create_task(withdraw_money(900))

    await task1
    await task2
    print(f'Остаток средств {bank_account}р')

asyncio.run(main())
