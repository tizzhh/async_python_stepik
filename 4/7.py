import asyncio


async def task(lock):
    print('task trying to get the lock')

    async with lock:
        print('trying again to get the lock')

        async with lock:
            ...


async def main():
    lock = asyncio.Lock()
    await task(lock)


asyncio.run(main())
