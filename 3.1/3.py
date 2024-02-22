import asyncio


async def cook_dish(n):
    print(f'{n} began cooking')
    await asyncio.sleep(n)
    print(f'{n} finished cooking')
    return f'meal of chef {n}'


async def main():
    tasks = [asyncio.create_task(cook_dish(n)) for n in range(1, 4)]
    print(await asyncio.gather(*tasks))


asyncio.run(main())
