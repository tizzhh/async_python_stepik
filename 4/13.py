import asyncio


bank_account = 1000


async def withdraw(amount):
    global bank_account
    if bank_account >= amount:
        print(f'withdraw of {amount} successful')
        await asyncio.sleep(1)
        bank_account -= amount


async def main():
    task1 = asyncio.create_task(withdraw(900))
    task2 = asyncio.create_task(withdraw(900))
    await asyncio.gather(task1, task2)
    print(bank_account)


asyncio.run(main())
