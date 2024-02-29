import asyncio


async def monitor_base(task_name, status_list):
    for status in status_list:
        await asyncio.sleep(0.1)
        print(f"[{task_name}] Статус проверки: {status}")
        if status == 'Катастрофически':
            print(
                f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка..."
            )


async def monitor_cpu(status_list):
    await monitor_base(asyncio.current_task().get_name(), status_list)


async def monitor_memory(status_list):
    await monitor_base(asyncio.current_task().get_name(), status_list)


async def monitor_disk_space(status_list):
    await monitor_base(asyncio.current_task().get_name(), status_list)


async def main():
    status_list = [
        "Отлично",
        "Хорошо",
        "Удовлетворительно",
        "Средне",
        "Пониженное",
        "Ниже среднего",
        "Плохо",
        "Очень плохо",
        "Критично",
        "Катастрофически",
    ]
    task1 = asyncio.create_task(monitor_cpu(status_list), name='CPU')
    task2 = asyncio.create_task(monitor_memory(status_list), name='Память')
    task3 = asyncio.create_task(
        monitor_disk_space(status_list), name='Дисковое пространство'
    )

    await asyncio.gather(task1, task2, task3)


asyncio.run(main())
