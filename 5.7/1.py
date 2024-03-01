import asyncio


async def my_coro(name, delay):
    """Асинхронная задача, которая просто ждет указанное время."""
    print(f'Задача {name} началась, будет выполняться {delay} секунд(ы).')
    await asyncio.sleep(delay)
    print(f'Задача {name} завершена.')
    return f'результат {name}'


async def main():
    # Создаем список задач
    coroutines = [my_coro(f"задача_{i}", i) for i in range(1, 4)]

    # Преобразуем корутины в задачи
    tasks = [asyncio.create_task(c) for c in coroutines]

    # Запускаем задачи и ждем их выполнения с таймаутом
    print("Запуск задач...")
    done, pending = await asyncio.wait(
        tasks, timeout=2, return_when=asyncio.ALL_COMPLETED
    )

    # Проверяем, какие задачи выполнены, а какие еще в ожидании
    print(f"\nЗавершенные задачи: {[d.result() for d in done]}")
    if pending:
        print(f"Ожидающие задачи: {pending}")
        # Опционально: Можно отменить оставшиеся задачи, если это необходимо
        for task in pending:
            print(f"Отмена {task}")
            task.cancel()
    else:
        print("Все задачи завершены.")


# Запускаем главную корутину
asyncio.run(main())
