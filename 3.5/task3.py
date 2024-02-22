import asyncio


max_counts = {
    'Counter 1': 13,
    'Counter 2': 7,
}


async def counter(counter: str, delay: int):
    for i in range(1, max_counts[counter] + 1):
        print(f'{counter}: {i}')
        await asyncio.sleep(delay)


async def main():
    counter1 = asyncio.create_task(counter('Counter 1', 1))
    counter2 = asyncio.create_task(counter('Counter 2', 1))
    await counter1
    await counter2


asyncio.run(main())
