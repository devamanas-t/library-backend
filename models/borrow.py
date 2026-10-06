from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,DateTime
from database import Base


class Borrow(Base):
    __tablename__ = "borrow_table"
    book_id = Column(Integer,ForeignKey("book_table.book_id"))
    user_id = Column(Integer,ForeignKey("user_table.user_id"))
    borrow_id = Column(Integer,primary_key=True)
    
    borrow_start = Column(DateTime)
    borrow_end = Column(DateTime)
    return_date = Column(DateTime)

    #time login will calculate on the borrow router