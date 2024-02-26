import asyncio


shared_resource = 0


async def update_resource():
    global shared_resource
    print('begin update of shared_resource')
    temp = shared_resource
    await asyncio.sleep(1)
    shared_resource = temp + 1
    print('update of shared_resource complete')


async def main():
    await asyncio.gather(update_resource(), update_resource())
    print(shared_resource)


asyncio.run(main())
