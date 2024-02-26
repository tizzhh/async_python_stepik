import asyncio
import aiohttp


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            return data


async def process_data(data):
    print(f'recieved data: {data}')


async def long_polling(url):
    while True:
        await asyncio.sleep(3)
        data = await fetch_data(url)
        if data:
            await process_data(data)


async def main():
    task = asyncio.create_task(
        long_polling("https://jsonplaceholder.typicode.com/posts")
    )
    await task


asyncio.run(main())
