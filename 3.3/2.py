import asyncio
import random


async def boil_water(time):
    print('boiling')
    await asyncio.sleep(time)
    print('boiled')


async def chop_vegetables():
    print('began cutting')
    await asyncio.sleep(random.randint(2, 4))
    print('cut')


async def prepare_dinner():
    await asyncio.gather(boil_water(5), chop_vegetables())


asyncio.run(prepare_dinner())
