import asyncio


async def print_message():
    while True:
        print('func imitation')
        await asyncio.sleep(1)


async def interrupt_handler(interrupt_flag):
    while True:
        await asyncio.sleep(0.5)
        if interrupt_flag.is_set():
            print('interrupt!')
            interrupt_flag.clear()
            break


async def main():
    interrupt_flag = asyncio.Event()
    asyncio.create_task(print_message())
    task2 = asyncio.create_task(interrupt_handler(interrupt_flag))
    while True:
        await asyncio.sleep(3)
        interrupt_flag.set()
        await task2
        task2 = asyncio.create_task(interrupt_handler(interrupt_flag))


asyncio.run(main())
