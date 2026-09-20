from fastapi import FastAPI
from models import book,user
from database import engine,Base
from routers import books,users #connectin the book.py


print(Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(books.router)
app.include_router(users.router)