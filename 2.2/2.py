import asyncio


async def fetch_data():
    print('Loading')
    await asyncio.sleep(2)
    return 'Data'


async def process_data():
    print('proessing')
    await asyncio.sleep(1)
    return 'data processed'


async def main():
    fetched_data = await fetch_data()
    processed_data = await process_data()
    print(fetched_data, processed_data)


asyncio.run(main())
