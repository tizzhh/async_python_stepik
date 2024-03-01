import asyncio


async def task_func(task_id):
    print(
        f"Задача {task_id} выполнена"
    )  # Выводим сообщение о выполнении задачи
    return f"Результат задачи {task_id}"  # Возвращаем результат задачи


async def main():
    tasks = [
        asyncio.create_task(task_func(i)) for i in range(5)
    ]  # Создаем несколько задач
    _, pending = await asyncio.wait(tasks)  # Ожидаем завершения всех задач
    assert (
        not pending
    ), f"{len(pending)} ожидающих задач"  # Проверяем, что все задачи завершены
    for task in tasks:
        print(
            f"Результат задачи {task.get_coro()}:", task.result()
        )  # Выводим результат каждой задачи


asyncio.run(main())
