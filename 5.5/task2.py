import asyncio
import itertools

spells = {
    "Огненный шар": 3,
    "Ледяная стрела": 2,
    "Щит молний": 6,
}

students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]

max_cast_time = 5

type_of_msg = 1


async def cast_spell(student, spell, cast_time):
    await asyncio.sleep(cast_time)
    if type_of_msg == 1:
        print(f"{student} успешно кастует {spell} за {cast_time} сек.")
    else:
        print(
            f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. {student} успешно завершает заклинание с помощью shield."
        )


async def main():
    tasks = [
        asyncio.shield(
            asyncio.create_task(
                cast_spell(student, spell, cast_time),
                name=f'{student} {spell}',
            )
        )
        for student, (spell, cast_time) in itertools.product(
            students, spells.items()
        )
    ]
    global type_of_msg
    try:
        await asyncio.wait_for(asyncio.gather(*tasks), max_cast_time)
    except asyncio.TimeoutError:
        type_of_msg = 0

    await asyncio.sleep(max(spells.values()))


asyncio.run(main())
