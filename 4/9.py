import asyncio


async def coro_a(event_a, event_b):
    print('coro a begins')
    try:
        await asyncio.wait_for(event_b.wait(), timeout=2)
    except asyncio.TimeoutError:
        print('coro a ended wait because of timeout')
    event_a.set()
    print('coro a done')


async def coro_b(event_b, event_c):
    print('coro b begins')
    await event_c.wait()
    print('coro b waits coro c')
    event_b.set()


async def coro_c(event_c, event_a):
    print('coro c begins')
    await event_a.wait()
    print('coro c waits coro a')
    event_c.set()


async def main():
    event_a = asyncio.Event()
    event_b = asyncio.Event()
    event_c = asyncio.Event()

    await asyncio.gather(
        coro_a(event_a, event_b),
        coro_b(event_b, event_c),
        coro_c(event_c, event_a),
    )


asyncio.run(main())
