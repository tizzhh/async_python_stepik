import asyncio


async def cor_1():
    print('Coroutine 1 is done')


async def cor_2():
    print('Coroutine 2 is done')


async def cor_3():
    print('Coroutine 3 is done')


async def main():
    cors = (cor_1, cor_2, cor_3)
    asyncio.gather(*(asyncio.create_task(cor()) for cor in cors))


asyncio.run(main())
