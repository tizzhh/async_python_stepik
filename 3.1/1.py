import time
import asyncio


async def coro(num, seconds):
    print(f'coro{num} began')
    await asyncio.sleep(seconds)
    print(f'coro{num} ended')


async def main():
    coro1 = coro(1, 2)
    coro2 = coro(2, 1)

    await coro2
    await coro1


start = time.time()
asyncio.run(main())
print(time.time() - start)
