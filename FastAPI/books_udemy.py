from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def first_api():
    return {"message": "Hello World"}

BOOKS = [
    {'title': 'title one ', 'author': 'author one', 'category': 'science '}
]

@app.get("/books")
async def read_all_books():
    return BOOKS

