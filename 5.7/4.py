import asyncio


async def foo():
    print("Запущена корутина foo")
    await asyncio.sleep(5)
    print("Явное переключение контекста обратно на 'foo'")


async def bar():
    print("Запущена корутина bar")
    await asyncio.sleep(3)
    print("Явное переключение контекста обратно на 'bar'")


async def main():
    tasks = [asyncio.create_task(foo()), asyncio.create_task(bar())]
    done, pending = await asyncio.wait(
        tasks, return_when=asyncio.FIRST_COMPLETED
    )

    for task in done:
        print("Задание завершено: ", task)
    for task in pending:
        print("Задание ожидает выполнения: ", task)


asyncio.run(main())
