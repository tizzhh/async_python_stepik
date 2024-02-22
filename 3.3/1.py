import asyncio


async def read_data_from_file(filename):
    print(f'reading from {filename}')
    await asyncio.sleep(2)
    print(f'reading from {filename} done')
    return f'data from {filename}'


async def send_data_to_internet(data):
    print('sending data')
    await asyncio.sleep(3)
    print('sending complete')


async def main():
    filename = 'main.txt'
    file_data = await read_data_from_file(filename)
    await send_data_to_internet(file_data)


asyncio.run(main())
