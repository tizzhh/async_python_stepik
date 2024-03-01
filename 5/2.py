import asyncio


async def my_coro():
    await asyncio.sleep(2)
    return 'hello world'


async def main():
    task = asyncio.create_task(my_coro())
    try:
        await asyncio.wait_for(asyncio.shield(task), timeout=1)
    except asyncio.exceptions.TimeoutError:
        print('timeout')

        res = await task
        print(res)


asyncio.run(main())
