# import asyncio


# class Room:
#     def __init__(self) -> None:
#         self.lock = asyncio.Lock()

#     # async def use(self, name):
#     #     await self.lock.acquire()
#     #     try:
#     #         print(f'{name} entered the room')
#     #         await asyncio.sleep(1)
#     #         print(f'{name} exited the room')
#     #     finally:
#     #         self.lock.release()

#     async def use(self, name):
#         async with self.lock:
#             print(f'{name} entered the room')
#             await asyncio.sleep(1)
#             print(f'{name} exited the room')


# async def person(name, room):
#     print(f'{name} wants to enter the room')
#     await room.use(name)

# async def main():
#     room = Room()

#     await asyncio.gather(
#         person('Alex', room),
#         person('Aboba', room),
#         person('Andrey', room),
#     )

# asyncio.run(main())

import asyncio


async def task(lock, name):
    try:
        await lock.acquire()
        print(f"{name} захватил мьютекс.")
        await asyncio.sleep(1)
        if name == "Task 1":
            raise Exception("Ошибка в задаче 1")
        await asyncio.sleep(1)
    finally:
        lock.release()
        print(f"{name} освободил мьютекс.")


async def main():
    lock = asyncio.Lock()
    results = await asyncio.gather(
        task(lock, "Task 1"), task(lock, "Task 2"), return_exceptions=True
    )
    print(results)


asyncio.run(main())
