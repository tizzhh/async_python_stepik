import asyncio


async def download_file(url):
    # Начало загрузки файла
    print(f"Начинается загрузка {url}")
    await asyncio.sleep(3)  # Имитация загрузки файла
    # Завершение загрузки файла
    print(f"Загрузка завершена {url}")


async def process_file(filename):
    # Начало обработки файла
    print(f"Начинается обработка {filename}")
    await asyncio.sleep(2)  # Имитация обработки файла
    # Завершение обработки файла
    print(f"Обработка завершена {filename}")


async def download_and_process(url, filename):
    # Запуск задач асинхронно
    task1 = asyncio.ensure_future(download_file(url))
    task2 = asyncio.ensure_future(process_file(filename))

    # Ожидание завершения обеих задач
    await asyncio.gather(task1, task2)


async def main():
    # Списки URL и имен файлов
    urls = [
        "http://example.com/file1",
        "http://example.com/file2",
        "http://example.com/file3",
    ]
    filenames = ["file1.txt", "file2.txt", "file3.txt"]

    # Создание и запуск задач на загрузку и обработку
    tasks = [
        asyncio.ensure_future(download_and_process(url, filename))
        for url, filename in zip(urls, filenames)
    ]

    # Ожидание завершения всех задач
    await asyncio.gather(*tasks)


# Запуск главной функции
asyncio.run(main())
