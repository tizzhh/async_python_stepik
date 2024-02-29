import asyncio


async def analyze_news(keyword, news_list, delay):
    for news in news_list:
        if keyword in news:
            await asyncio.sleep(delay)
            print(f"Найдено соответствие для '{keyword}': {news}")


async def main():
    # Создаем асинхронные задачи для каждой корутины с разными ключевыми словами и задержками
    task1 = asyncio.create_task(analyze_news('COVID-19', news_list, 1))
    task2 = asyncio.create_task(analyze_news('игр', news_list, 1))
    task3 = asyncio.create_task(analyze_news('новый вид', news_list, 1))

    # Ожидаем выполнения всех задач
    await asyncio.gather(task1, task2, task3)


asyncio.run(main())
