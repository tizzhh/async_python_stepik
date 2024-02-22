import asyncio


async def compute_square(x):
    print(f'computing square of {x}')
    await asyncio.sleep(1)
    return x * x


async def main():
    results = [asyncio.create_task(compute_square(i)) for i in range(10)]
    completed, pending = await asyncio.wait(results)
    for task in completed:
        print(f'result {task.result()}')


asyncio.run(main())
