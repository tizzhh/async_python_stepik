import asyncio


async def long_running_task(t):
    print(f"Task {t} started")
    await asyncio.sleep(t)
    print(f"Task {t} finished")


async def main():
    tasks = [
        asyncio.wait_for(asyncio.create_task(long_running_task(t)), timeout=2)
        for t in range(5)
    ]
    try:
        await asyncio.gather(*tasks)
    except asyncio.TimeoutError:
        print("Timeout, aborting")


if __name__ == '__main__':
    asyncio.run(main())
