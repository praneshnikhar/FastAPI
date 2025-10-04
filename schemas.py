from pydantic import BaseModel

# class Blog(BaseModel):
#     title:str
#     body:str
    
# class ShowBlog(Blog):
#     title:str
#     body:str
    
#     class Config():
#         orm_mode = True
        
# class User(BaseModel):
#     name:str
#     email:str
#     password:str 

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class PostCreate(PostBase):
    pass


