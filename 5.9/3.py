import asyncio
import threading


async def task1(id, loop):
    print(f"Task {id} starting, loop = {loop}")
    await asyncio.sleep(2)
    print(f"Task {id} completed")


async def task2(id, loop):
    print(f"Task {id} starting, loop = {loop}")
    await asyncio.sleep(3)
    print(f"Task {id} completed")


def start_loop(loop, coroutine):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(coroutine)


async def main():
    loop1 = asyncio.new_event_loop()
    loop2 = asyncio.new_event_loop()

    coroutine1 = task1(1, loop1)
    coroutine2 = task2(2, loop2)

    thread1 = threading.Thread(
        target=start_loop,
        args=(
            loop1,
            coroutine1,
        ),
    )
    thread2 = threading.Thread(
        target=start_loop,
        args=(
            loop2,
            coroutine2,
        ),
    )

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


asyncio.run(main())
