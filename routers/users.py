from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.user import User
from schemas import user

#fetch some useful function from books.py
from routers.books import errorHandling

router = APIRouter()

@router.post("/user/create",response_model=user.UserResponse)
def create_user(user_data:user.UserCreate,db:Session = Depends(get_db)):
    db_user = db.query(User).filter(
        User.user_name == user_data.user_name and User.phone_no == user_data.phone_no
    ).all() #checks the user alredy excists or not
    
    if db_user:
        raise errorHandling()#find if the code runs after this raise condition
    db_user=User(**user_data.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    

