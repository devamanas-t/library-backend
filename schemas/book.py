from pydantic import BaseModel


class ModelConfig(BaseModel):
    model_config={
        "from_attributes":True
    }

class BookBase(ModelConfig):

    book_id : int 
    book_name :str
    auther_name :str
    journal :str
    no_of_books :int
    is_available :bool
    

class BookCreate(ModelConfig):
    book_id : int 
    book_name: str
    auther_name:str
    journal:str
    no_of_books:int

class BookRespose(ModelConfig):
    book_name:str
    auther_name:str
    journal:str
    no_of_books:int
    is_available:bool

class BookUpdate(BookBase):
    pass
    

