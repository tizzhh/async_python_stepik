import asyncio


async def simulate_long_running_task(name, delay):
    print(f"Задача '{name}' началась, будет выполнена за {delay} секунд.")
    await asyncio.sleep(delay)
    print(f'task {name} finished')
    return f'result of task {name}'


async def main():
    cor = simulate_long_running_task('task1', 3)
    future = asyncio.ensure_future(cor)
    await future

    res = future.result()
    print(f'result of future: {res}')


asyncio.run(main())
