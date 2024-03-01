import asyncio


async def equipment_request(request):
    await asyncio.sleep(1)
    return request.split()[0] + 'is Ok!'


async def send_requests():
    tasks = [
        asyncio.create_task(equipment_request(req)) for req in equipment_list
    ]
    await asyncio.gather(*tasks)
    waiting_time = query_time()
    print(
        f'На отправку {len(equipment_list)} запросов потребовалось {waiting_time} секунд!'
    )
