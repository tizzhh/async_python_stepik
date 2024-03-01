import asyncio
import itertools

spells = {
    "Огненный шар": 3,
    "Ледяная стрела": 2,
    "Щит молний": 6,
}

students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]

max_cast_time = 5


async def cast_spell(student, spell, cast_time, shell=0):
    try:
        await asyncio.sleep(cast_time)
        print(
            [
                f"{student} успешно кастует {spell} за {cast_time} сек.",
                f"Ученик {student} не справился с заклинанием {spell}, и учитель накладывает щит. {student} успешно завершает заклинание с помощью shield.",
            ][shell]
        )
    except asyncio.CancelledError:
        await asyncio.shield(cast_spell(student, spell, cast_time, 1))
        print(
            [
                f"{student} успешно кастует {spell} за {cast_time} сек.",
                f"Ученик {student} не справился с заклинанием {spell}, и учитель накладывает щит. {student} успешно завершает заклинание с помощью shield.",
            ][1]
        )


async def main():
    tasks = [
        asyncio.wait_for(
            asyncio.shield(
                asyncio.create_task(
                    cast_spell(student, spell, cast_time, 0),
                    name=f'{student} {spell}',
                )
            ),
            timeout=max_cast_time,
        )
        for student, (spell, cast_time) in itertools.product(
            students, spells.items()
        )
    ]

    try:
        await asyncio.gather(*tasks)
    except asyncio.TimeoutError:
        ...
    await asyncio.sleep(10)


asyncio.run(main())
