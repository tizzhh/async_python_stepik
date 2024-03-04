import asyncio


async def sample_coroutine():
    print("Hello, asyncio!")


# Используем asyncio.ensure_future() с корутиной и проверяем тип возвращаемого объекта
task = asyncio.ensure_future(sample_coroutine())

# Вывод типа объекта
print(type(task))
