import asyncio

max_counts = {"Counter 1": 10, "Counter 2": 5, "Counter 3": 15}

delays = {"Counter 1": 1, "Counter 2": 2, "Counter 3": 0.5}


async def counter(counter: str):
    for i in range(1, max_counts[counter] + 1):
        await asyncio.sleep(delays[counter])
        print(f'{counter}: {i}')


async def main():
    tasks = [asyncio.create_task(counter(task)) for task in max_counts]
    await asyncio.gather(*tasks)


asyncio.run(main())
