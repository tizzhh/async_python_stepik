import asyncio


async def async_func():
    def sync_func():
        return 42

    res = sync_func()
    print(res)


asyncio.run(async_func())
