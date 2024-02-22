import asyncio
from random import randint


async def my_task(i):
    print(f'task {i}')
    await asyncio.sleep(randint(1, 4))
    print(f'task {i} done')


async def main():
    tasks = []
    for x in range(5):
        tasks.append(asyncio.create_task(my_task(x)))
    await asyncio.gather(*tasks)


asyncio.run(main())
