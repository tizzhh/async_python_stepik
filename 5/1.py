import asyncio


async def task_func(duration):
    name = asyncio.current_task().get_name()
    print(f'task {name} will finish in {duration} secs')
    await asyncio.sleep(duration)
    print(f'task {name} is done')


async def exeptor(duration):
    try:
        await asyncio.sleep(duration)
        print(
            f'task {asyncio.current_task().get_name()} caused and exception in {duration} secs'
        )
        raise Exception('error happened')
    except Exception as e:
        print(
            f'during task {asyncio.current_task().get_name()} an exception happened: {e}'
        )


async def main():
    task1 = asyncio.create_task(task_func(3), name='first')
    task2 = asyncio.create_task(task_func(1), name='second')
    task3 = asyncio.create_task(exeptor(2), name='exeption')
    await asyncio.gather(task1, task2, task3)


asyncio.run(main())
