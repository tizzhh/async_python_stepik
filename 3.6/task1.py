import asyncio


async def set_future_result(value, delay: int):
    print(
        f"Задача начата. Установка результата '{value}' через {delay} секунд."
    )
    await asyncio.sleep(delay)
    print("Результат установлен.")
    return value


async def create_and_use_future():
    future = asyncio.ensure_future(set_future_result('Успех', 2))
    if not future.done():
        print("Состояние Future до выполнения: Ожидание")
    else:
        print("Состояние Future до выполнения: Завершено")
    print("Задача запущена, ожидаем завершения...")
    res = await future
    if not future.done():
        print("Состояние Future после выполнения: Ожидание")
    else:
        print("Состояние Future после выполнения: Завершено")
    return res


async def main():
    result = await create_and_use_future()
    print("Результат из Future:", result)


asyncio.run(main())
