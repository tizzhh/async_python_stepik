import asyncio


async def fetch_data(delay: int, source: str) -> str:
    await asyncio.sleep(delay)
    return f'data from {source}'


async def main():
    sources = ['source ' + str(i) for i in range(1, 4)]
    for source in sources:
        data = await fetch_data(1, source)
        print(data)


asyncio.run(main())
