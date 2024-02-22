import asyncio


async def coro_1():
    print('coro_1 says, hello coro_2!')


async def coro_2():
    print('coro_2 says, hello coro_1!')


async def main():
    await coro_1()
    await coro_2()


asyncio.run(main())
