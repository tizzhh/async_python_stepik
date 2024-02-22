import asyncio


chef_list = ['', 'aboba', 'aboba1', 'aboba2']


async def cook_order(order_num, dish):
    print(
        f'chef {chef_list[order_num]} began cooking order num {order_num}: {dish}'
    )
    await asyncio.sleep(2)
    print(f'order {order_num}: {dish} is ready!')
    return f'{dish} for order {order_num}'


async def serve_order(order_num, dish):
    cooked_dish = await cook_order(order_num, dish)
    print(f'waiter serving {cooked_dish}')


async def manamger():
    orders = ((1, 'slaad'), (2, 'steak'), (3, 'soup'))
    await asyncio.gather(
        *(
            asyncio.create_task(serve_order(order_num, dish))
            for order_num, dish in orders
        )
    )


asyncio.run(manamger())
