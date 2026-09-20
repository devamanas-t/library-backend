from pydantic import BaseModel

class ModelConfig(BaseModel):
    model_config={
        "from_attributes":True
    }
class UserBase(ModelConfig):
    user_name:str
    user_age:int
    phone_no:str
    user_membership:bool

class UserCreate(UserBase):
    user_place:str

class UserResponse(UserBase):#for response model
    user_id:int
    user_place:str
    

class UserUpdate(UserCreate):
    pass
