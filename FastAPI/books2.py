from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()

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

class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length= 1, max_length=260)
    rating: float = Field(gt=0, lt=6)

    model_config = {
        "JSON_schema_extra":{
            "example": {
                "title": "new book title",
                "author": "who is Author",
                "description": "description this book",
                "rating": "1~5 number "
            }
        }
    }


BOOKS=[
    Book(1, "How to Use FastApi", "Tom", "it is a good book, very nice with FastAPI.", 4.5),
    Book(2, "learning JavaScript", "Roby", "it is a learning JavaScript book, we call JS cookbook", 5),
    Book(3, "Coding with TypeScript", "Jerry", "TypeScript is super grow language, will instead of JS", 4.3),
    Book(4, "Work with Python", "Zack", "Python is top one language work with Data Engineer ", 5),
    Book(5, "Think in Java", "Ross", "thinking in Java, use Java to create any kind of project ", 5),
    Book(6, "Think in GoLang", "Peter", "Golang is super fast with micro-servers and web application", 4.5)
]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    # return "Successful Create Book"

def find_book_id(book: Book):
    book.id= 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book