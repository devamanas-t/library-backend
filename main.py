from fastapi import FastAPI,Depends,HTTPException
from database import SessionLocal,engine,Base
import schema,model
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/book/create",response_model=schema.BookCreate)#here full including the id stuff
def create_book(book:schema.BookBase,db:Session = Depends(get_db)):#input or user what see 
    db_book=model.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

#this will return all books from the db (but it is not good coz maybe 1000+above records)
@app.get("/books",response_model = list[schema.BookBase])#what user see or response
def show_all_books(db:Session = Depends(get_db)):
    books = db.query(model.Book).all()
    return books


@app.get("/books/name/{book_name}",response_model=schema.BookRespose)
def show_with_name(book_name:str,db:Session = Depends(get_db)):
    book = db.query(model.Book).filter(model.Book.book_name == book_name).first()
    return book


@app.get("/books/auther/{book_auther}",response_model=schema.BookRespose)
def show_with_auther(book_auther:str,db:Session = Depends(get_db)):
    auther = db.query(model.Book).filter(model.Book.auther_name==book_auther).first()
    return auther


@app.get("/books/journal/{book_journal}",response_model=list[schema.BookRespose])
def show_all_with_journal(book_journal:str,db:Session = Depends(get_db)):
    journal = db.query(model.Book).filter(model.Book.journal == book_journal).all()
    return journal


@app.put("/books/update/name/{book_name}",response_model=schema.BookUpdate)
def update_by_name(book_name:str,book:schema.BookUpdate,db:Session = Depends(get_db)):
    db_book = db.query(model.Book).filter(model.Book.book_name == book_name).first()
    if not db_book:
        raise HTTPException(status_code=404,detail="Book not found")
    for key,value in book.model_dump().items():# key = "book_name"  value = "Harry Potter" for next for it change key = "author"  value = "J.K. Rowling"
        setattr(db_book,key,value)#db_book.book_name(key) = "Harry Potter"(value)
    db.commit()
    db.refresh(db_book)
    return db_book

#now create another put for id then simple delete too then optimise it maximum 

    