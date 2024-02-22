import asyncio


async def my_cor(arg):
    await asyncio.sleep(1)
    print(f'cor created with {arg}')


async def main():
    future = asyncio.ensure_future(my_cor('future'))
    task = asyncio.create_task(my_cor('task'))

    print(f'ensure_future type: {type(future)}')
    print(f'create_task type: {type(task)}')

    await future
    await task


asyncio.run(main())
