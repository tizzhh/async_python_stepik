import asyncio


places = [
    "начинает путешествие",
    "находит загадочный лес",
    "переправляется через реку",
    "встречает дружелюбного дракона",
    "находит сокровище",
]


async def counter(name, delay):
    for place in places:
        await asyncio.sleep(delay)
        print(f'{name} {place}...')


async def main():
    task1 = asyncio.create_task(counter('Искатель приключений', 1))
    task2 = asyncio.create_task(counter('Храбрый рыцарь', 1))
    task3 = asyncio.create_task(counter('Отважный пират', 1))

    await asyncio.gather(task1, task2, task3)


asyncio.run(main())
