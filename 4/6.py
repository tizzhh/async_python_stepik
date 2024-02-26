import asyncio


async def car(lock1, lock2, name):
    print(f'Car {name} approaching the intersection')
    await asyncio.sleep(1)
    async with lock1:
        print(f'Car {name} waiting on the intersection')
        await asyncio.sleep(1)
        async with lock2:
            print(f'Car {name} leaves the intersection')


async def main():
    north_south = asyncio.Lock()
    easth_west = asyncio.Lock()

    await asyncio.gather(
        car(north_south, easth_west, 'North-south'),
        car(easth_west, north_south, 'East-west'),
        car(north_south, easth_west, 'south-north'),
        car(easth_west, north_south, 'west-east'),
    )


asyncio.run(main())
