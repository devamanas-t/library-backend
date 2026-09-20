from sqlalchemy import Column,Integer,String,Boolean
from database import Base

class User(Base):
    __tablename__ = "user_table"
    user_id = Column(Integer,primary_key=True,autoincrement=True)
    user_name = Column(String,nullable=False,index=True)
    user_age = Column(Integer)
    phone_no = Column(String,index=True)
    user_place = Column(String)
    user_membership = Column(Boolean)