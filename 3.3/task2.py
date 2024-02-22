import asyncio
import time


async def task1():
    print("Начинаем задачу 1")
    await asyncio.sleep(1)
    print("Привет из корутины task1")
    await asyncio.sleep(1)
    print("Задача 1 завершилась")


async def task2():
    print("Начинаем задачу 2")
    await asyncio.sleep(2)
    print("Привет из корутины task2")
    await asyncio.sleep(2)
    print("Задача 2 завершилась")


async def task3():
    print("Начинаем задачу 3")
    await asyncio.sleep(3)
    print("Привет из корутины task3")
    await asyncio.sleep(3)
    print("Задача 3 завершилась")


async def main():
    task_1 = asyncio.create_task(task1())
    task_2 = asyncio.create_task(task2())
    task_3 = asyncio.create_task(task3())

    await task_1
    await task_2
    await task_3


start = time.time()
asyncio.run(main())
print(time.time() - start)
