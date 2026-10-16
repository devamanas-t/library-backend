from pydantic import BaseModel
from datetime import datetime

class ModelConfig(BaseModel):
    model_config = {
        "from_attributes":True
    }
class BorrowBase(ModelConfig):
    user_id:int
    book_id:int
    borrow_start:datetime |None = None

class CreateBorrow(BorrowBase):
    pass

class BorrowResponse(CreateBorrow):
    borrow_id:int
    user_name:str
    book_name:str
    phone_no:str
    borrow_start:datetime
    return_date:datetime | None = None
    borrow_end:datetime 

class BorrowUpdate(BorrowBase):
    pass

class BorrowReturn(ModelConfig):
    return_date:datetime | None = None

class BorrowResponseNew(ModelConfig):
    user_name:str
    phone_no:str
    book_name:str
    borrow_start:datetime
    borrow_end:datetime 


