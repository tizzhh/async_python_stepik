import asyncio


async def activate_portal(x):
    print(f'Активация портала в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x):
    print(f'Телепортация в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x + 2


async def recharge_portal(x):
    print(f'Подзарядка портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 3


async def check_portal_stability(x):
    print(f'Проверка стабильности портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x + 4


async def restore_portal(x):
    print(f'Восстановление портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 5


async def close_portal(x):
    print(f'Закрытие портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x - 1


async def portal_operator():
    funcs = {
        'Результат активации портала': activate_portal,
        'Результат телепортации': perform_teleportation,
        'Результат подзарядки портала': recharge_portal,
        'Результат проверки стабильности': check_portal_stability,
        'Результат восстановления портала': restore_portal,
        'Результат закрытия портала': close_portal,
    }
    results = await asyncio.gather(
        *[
            asyncio.ensure_future(func(i + 2))
            for i, func in enumerate(funcs.values())
        ]
    )

    for i, res in enumerate(results):
        print(
            list(funcs.keys())[i]
            + f': {res} единиц '
            + ('энергии' if i % 2 == 0 else 'времени')
        )


asyncio.run(portal_operator())
