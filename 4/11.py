import asyncio


async def task(num, locks):
    sorted_locks = sorted(locks, key=id)
    print(f'task {num} trying to get lock1')
    async with sorted_locks[0]:
        print(f'task {num} got the lock1')
        await asyncio.sleep(1)
        print(f'task {num} trying to get lock2')
        async with sorted_locks[1]:
            print(f'task {num} got the lock2')
            await asyncio.sleep(2)
    print(f'task {num} done')


async def main():
    lock1 = asyncio.Lock()
    lock2 = asyncio.Lock()

    await asyncio.gather(
        task(1, [lock1, lock2]),
        task(2, [lock2, lock1]),
    )


asyncio.run(main())
