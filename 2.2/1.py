import asyncio

async def fetch_data():
    print('Begin')
    await asyncio.sleep(2)
    print('Load complete')
    return {'data': 123}

async def main():
    tasks = [fetch_data() for _ in range(10)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())