import asyncio


shared_resource = 0
lock = asyncio.Lock()


async def update_resourse():
    global shared_resource
    print('begin update of shared_resource')
    async with lock:
        temp = shared_resource
        await asyncio.sleep(1)
        shared_resource = temp + 1
    print('update complete')


async def main():
    await asyncio.gather(update_resourse(), update_resourse())
    print(shared_resource)


asyncio.run(main())
