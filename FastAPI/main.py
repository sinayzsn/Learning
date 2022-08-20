from typing import Optional

from fastapi import FastAPI


app = FastAPI()

BOOKS = []

@app.get("/")
async def read_all_books(books_to_return: Optional[int] = None):
    if len(BOOKS) < 1:
        create_books_no_api()

    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 0
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i])