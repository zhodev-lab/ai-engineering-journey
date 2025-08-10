from fastapi import FastAPI

app = FastAPI()

BOOKS = []

@app.get("/books")
async def read_all_books():
    return BOOKS


class Book:
    id:int
    title:str
    author:str
    description:str
    rating: float

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
    

BOOKS=[
    Book(1, "How to Use FastApi", "Tom", "it is a good book, very nice with FastAPI.", 4.5),
    Book(2, "learning JavaScript", "Roby", "it is a learning JavaScript book, we call JS cookbook", 5),
    Book(3, "Coding with TypeScript", "Jerry", "TypeScript is super grow language, will instead of JS", 4.3),
    Book(4, "Work with Python", "Zack", "Python is top one language work with Data Engineer ", 5),
    Book(5, "Think in Java", "Ross", "thinking in Java, use Java to create any kind of project ", 5),
    Book(6, "Think in GoLang", "Peter", "Golang is super fast with micro-servers and web application", 4.5)
]