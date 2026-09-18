from fastapi import FastAPI
from database import engine,Base
from routers import books #connectin the book.py

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(books.router)