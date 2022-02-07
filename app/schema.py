from datetime import datetime
from pydantic import BaseModel, EmailStr

class PostBase(BaseModel):
    title: str
    author: str
    content: str
    class Config: 
        orm_mode = True
        
class GetPost(PostBase):
    id: int
    created_at: datetime
    
class CreatePost(PostBase):
    pass

class UpdatePost(PostBase):
    pass

class User(BaseModel):
    email: EmailStr
    password: str
    created_at: datetime
    class Config: 
        orm_mode = True
        
class GetUser(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config: 
        orm_mode = True

class CreateUser(User):
    pass

class UpdateUser(User):
    pass

class UserLogin(BaseModel):
    email: EmailStr
    password: str