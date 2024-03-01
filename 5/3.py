import asyncio
import time
from random import random


async def coro(delay):
    start = time.time()
    value = random()
    print(f'Задача получила delay: {delay}')
    await asyncio.sleep(delay)
    print(f'Задача выполнена за {time.time()-start:.3f}')


async def main():
    # Создаем задачу со временем выполнения 3 секунды
    task = asyncio.create_task(coro(3))
    await asyncio.sleep(2)
    # Ожидаем выполнения task 1 секунду
    await asyncio.wait_for(task, timeout=1)


asyncio.run(main())
