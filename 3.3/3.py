import aiohttp
import asyncio


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    data = await fetch_data('http://python.org')
    print(data)


asyncio.run(main())
