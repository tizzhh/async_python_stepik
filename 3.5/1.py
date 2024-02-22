import asyncio


async def my_cor():
    await asyncio.sleep(1)
    print('task done')


async def main():
    task = asyncio.create_task(my_cor())
    print(type(task))
    await task


asyncio.run(main())
