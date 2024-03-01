import asyncio


async def activate_portal(x):
    print(f'Активация портала в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x):
    print(f'Телепортация в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x + 2


async def portal_operator():
    res = await asyncio.ensure_future(activate_portal(2))
    res2 = await asyncio.ensure_future(
        perform_teleportation(res if res <= 4 else 1)
    )
    print(f'Результат активации портала: {res} единиц энергии')
    print(f'Результат телепортации: {res2} единиц времени')


asyncio.run(portal_operator())
