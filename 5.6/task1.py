import asyncio


books_json = [
    {
        "Порядковый номер": 1,
        "Автор": "Rebecca Butler",
        "Название": "Three point south wear score organization.",
        "Год издания": "1985",
        "Наличие на полке": True,
    },
    {
        "Порядковый номер": 2,
        "Автор": "Mark Cole",
        "Название": "Drive experience customer somebody pressure.",
        "Год издания": "1985",
        "Наличие на полке": False,
    },
]


async def check_book(book):
    if not book["Наличие на полке"]:
        return f"{book['Порядковый номер']}: {book['Автор']}: {book['Название']} ({book['Год издания']})"


async def main():
    book_checks = [
        asyncio.create_task(check_book(book)) for book in books_json
    ]

    results = await asyncio.gather(*book_checks)
    for res in results:
        if res is not None:
            print(res)


asyncio.run(main())
