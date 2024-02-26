import asyncio


async def task(lock):
    print('task gets the lock')
    await lock.acquire()
    raise Exception('something bad happened')
    print('task frees the lock')
    lock.release()


async def main():
    lock = asyncio.Lock()
    asyncio.create_task(task(lock))
    await asyncio.sleep(1)
    print('main func gets the lock')
    await lock.acquire()
    lock.release()


asyncio.run(main())
