from sqlalchemy import Column,Integer,String,Boolean
from database import Base#latter have to mention the file path 


class Book(Base):
    __tablename__ = "book_table"
    book_id = Column(Integer,primary_key=True)
    book_name = Column(String,nullable=False,index=True)
    auther_name = Column(String,index=True)
    journal = Column(String,index=True)
    no_of_books = Column(Integer)
    is_available = Column(Boolean)