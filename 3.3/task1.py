import asyncio


async def task1():
    await asyncio.sleep(1)
    print('cour1')


async def task2():
    await asyncio.sleep(1)
    print('cour2')


async def main():
    asyncio.create_task(task1())
    await asyncio.create_task(task2())


asyncio.run(main())
