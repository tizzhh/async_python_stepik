import asyncio


DISTANCE = 100

runners = {
    "Молния Марк": 12.8,
    "Ветренный Виктор": 13.5,
    "Скоростной Степан": 11.2,
    "Быстрая Белла": 10.8,
}


async def run_lap(name, speed):
    time_needed = round(DISTANCE / speed, 2)
    await asyncio.sleep(time_needed)
    print(f"{name} завершил круг за {time_needed} секунд")


async def main(max_time=10):
    tasks = [
        asyncio.wait_for(run_lap(name, speed), timeout=max_time)
        for name, speed in runners.items()
    ]

    try:
        await asyncio.gather(*tasks)
    except asyncio.TimeoutError:
        ...


asyncio.run(main())
