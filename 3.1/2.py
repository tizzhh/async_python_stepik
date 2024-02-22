import time
import asyncio


async def coro(num, seconds):
    print(f'task{num} began')
    await asyncio.sleep(seconds)
    print(f'task{num} ended')


async def main():
    task1 = asyncio.create_task(coro(1, 2))
    task2 = asyncio.create_task(coro(2, 1))

    await task2
    await task1


start = time.time()
asyncio.run(main())
print(time.time() - start)
