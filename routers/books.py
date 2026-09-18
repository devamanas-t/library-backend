from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.book import Book
from schemas import book

router = APIRouter()

#functions lives here

def errorHandling():
    return HTTPException(status_code=404,detail="not found")

def updateBook(book,db_book):
    # key = "book_name"  value = "Harry Potter" for next for it change key = "author"  value = "J.K. Rowling"
    for key,value in book.model_dump().items():
        #db_book.book_name(key) = "Harry Potter"(value)
        setattr(db_book,key,value)
    return db_book


def fetch_from_db(db,book_name):
    db_book = db.query(Book).filter(Book.book_name == book_name).first()
    if not db_book:
        raise errorHandling()
    return db_book

#end of functions



#post for create new records

@router.post("/book/create",response_model=book.BookCreate)#here full including the id stuff
def create_book(book_data:book.BookBase,db:Session = Depends(get_db)):#input or user what see 
    db_book=Book(**book_data.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book



#this will return all books from the db (but it is not good coz maybe 1000+above records)
@router.get("/books",response_model = list[book.BookBase])#what user see or response
def show_all_books(db:Session = Depends(get_db)):
    db_books = db.query(Book).all()
    return db_books



#return by book name 
@router.get("/books/name/{book_name}",response_model=book.BookRespose)
def show_with_name(book_name:str,db:Session = Depends(get_db)):
    fetch_from_db(db,book_name)
    return db_book



#shows all
@router.get("/books/auther/{book_auther}",response_model=list[book.BookRespose])
def show_with_auther(book_auther:str,db:Session = Depends(get_db)):
    db_book_by_auther = db.query(Book).filter(Book.auther_name==book_auther).all()
    return db_book_by_auther



@router.get("/books/journal/{book_journal}",response_model=list[book.BookRespose])
def show_all_with_journal(book_journal:str,db:Session = Depends(get_db)):
    db_book_by_journal = db.query(Book).filter(Book.journal == book_journal).all()
    return db_book_by_journal



@router.put("/books/update/name/{book_name}",response_model=book.BookUpdate)
def update_by_name(book_name:str,book_data:book.BookUpdate,db:Session = Depends(get_db)):
    fetch_from_db(db,book_name)#get db_book from the function
    try:
        updateBook(book_data,db_book)   

        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception:
        db.rollback()
        raise


@router.put("/books/update/id/{book_id}",response_model=book.BookUpdate)
def update_by_id(book_id:int,book_data:book.BookUpdate,db:Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.book_id==book_id).first()
    if not db_book:
        raise errorHandling()
    try:
        updateBook(book_data,db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception:
        db.rollback()
        raise


@router.delete("/books/delete/id/{book_id}",response_model=book.BookBase)
def delete_by_id(book_id:int,db:Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.book_id == book_id).first()
    if not db_book:
        raise errorHandling()
    db.delete(db_book)
    db.commit()
    return