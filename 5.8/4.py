import asyncio


async def my_coroutine():
    await asyncio.sleep(1)
    print("Корутина выполнена")


async def main():
    # Создание задачи напрямую
    direct_task = asyncio.create_task(my_coroutine())

    # Передача уже существующей задачи в ensure_future
    ensured_task = asyncio.ensure_future(direct_task)

    print(f"Являются ли объекты идентичными: {direct_task is ensured_task}")


asyncio.run(main())
