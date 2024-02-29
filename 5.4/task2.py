import asyncio


async def countdown(name, seconds):
    if name == 'Квест на поиск сокровищ':
        for i in range(seconds, 0, -1):
            print(f"{name}: Осталось {i} сек. Найди скрытые сокровища!")
            await asyncio.sleep(0.5)
    else:
        for i in range(seconds, 0, -1):
            print(f"{name}: Осталось {i} сек. Беги быстрее, дракон на хвосте!")
            await asyncio.sleep(0.5)
    print(f"{name}: Задание выполнено! Что дальше?")


async def main():
    treasure_hunt = asyncio.create_task(
        countdown('Квест на поиск сокровищ', 10)
    )
    dragon_escape = asyncio.create_task(countdown('Побег от дракона', 5))

    await asyncio.gather(treasure_hunt, dragon_escape)


asyncio.run(main())
