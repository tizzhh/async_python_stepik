import asyncio
import random


class Pizzeria:
    def __init__(self, name) -> None:
        self.name = name

    async def make_pizza(self, order_id):
        cook_time = random.randint(2, 5)
        print(f'pizzeria {self.name} began cooking for {order_id}')
        await asyncio.sleep(cook_time)
        print(f'pizzeria {self.name} finished cooking for {order_id}')


async def main():
    pizzeria = Pizzeria('dodo')
    tasks = [pizzeria.make_pizza(i) for i in range(1, 6)]
    await asyncio.gather(*tasks)


asyncio.run(main())
