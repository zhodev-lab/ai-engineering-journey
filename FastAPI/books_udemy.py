from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def first_api():
    return {"message": "Hello World"}

BOOKS = [
    {'title': 'title one ', 'author': 'author one', 'category': 'science '},
    {'title': 'title two ', 'author': 'author two', 'category': 'math '}
]

@app.get("/books")
async def read_all_books():
    return BOOKS    

@app.get("/books{dynamic_param}")
async def read_all_books(dynamic_param):
    res = []
    for item in BOOKS:
        if item['title'].find(dynamic_param) >=0 or item['author'].find(dynamic_param) >=0:
            res.append(item)
    return { 'books' : res }
