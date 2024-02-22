import asyncio


async def do_some_work_1(x):
    print(f'job 1: {x}')
    await asyncio.sleep(x)
    return x * 2


async def do_some_work_2(x):
    print(f'job 2: {x}')
    await asyncio.sleep(x)
    return x * 2


async def main():
    future_1 = asyncio.ensure_future(do_some_work_1(2))
    res_1 = await future_1
    future_2 = asyncio.ensure_future(do_some_work_2(res_1))
    res_2 = await future_2
    print(res_1, res_2)


asyncio.run(main())
