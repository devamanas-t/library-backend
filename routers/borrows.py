from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.borrow import Borrow
from models.user import User
from models.book import Book
from schemas import borrow
from datetime import datetime,timedelta

#this fucntion later organized into another file
from routers.books import errorHandling

router = APIRouter()

@router.post("/borrow/create",response_model=borrow.BorrowResponse)
def crete_borrow(borrow_data:borrow.CreateBorrow,db:Session = Depends(get_db)):
    db_borrow = db.query(Borrow).filter(
        Borrow.user_id == borrow_data.user_id,Borrow.return_date == None
    ).first()
    if db_borrow:
        print("the user alrady lend a book")
        raise errorHandling()
        
    #logic for the date calculating
    borrow_start = borrow_data.borrow_start
    if borrow_start is None:
        borrow_start = datetime.now()
    borrow_end = borrow_start + timedelta(days=15)
    

    data = borrow_data.model_dump()
    data["borrow_start"] = borrow_start
    data["borrow_end"] = borrow_end

    db_borrow = Borrow(**data)
    db.add(db_borrow)
    db.commit()
    db.refresh(db_borrow)
    return db_borrow
@router.get("/borrow/get",response_model = list[borrow.BorrowResponseNew])
def show_none_return(db:Session = Depends(get_db)):
    db_borrow = (
        db.query(
            User.user_name,
            User.phone_no,
            Book.book_name,
            Borrow.borrow_start,
            Borrow.borrow_end
        )
        .join(User,Borrow.user_id == User.user_id)
        .join(Book,Borrow.book_id == Book.book_id)
        .filter(Borrow.return_date == None)
        .all()
    )
    return db_borrow
    
    
    