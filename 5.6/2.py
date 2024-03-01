import asyncio


async def my_coro(num):
    print(f'coro {num} began')
    await asyncio.sleep(num)
    if num % 2 == 0:
        raise Exception(f'error in coro {num}')
    print(f'coro {num} ended')
    return num


async def main():
    coros = [my_coro(i) for i in range(1, 6)]
    results = await asyncio.gather(*coros, return_exceptions=True)
    for res in results:
        if isinstance(res, Exception):
            print(f'error: {res}')
        else:
            print(res)


asyncio.run(main())
