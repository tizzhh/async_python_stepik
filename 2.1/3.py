import asyncio
import time

start = time.time()


async def sleeping(n):
    print(
        f"Начало выполнения длительной операции № {n}: {time.time() - start:.4f}"
    )
    await asyncio.sleep(1)
    print(f"Длительная операция № {n} завершена")
    return f'Результат Оп.№ {n}'


async def main():
    task = [sleeping(i) for i in range(1, 31)]
    all_results = await asyncio.gather(*task)
    print(f"Выполнено {len(all_results)} операций.")
    print(f"Программа завершена за {time.time() - start:.4f}")


asyncio.run(main())
