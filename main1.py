from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating : Optional[int] = None
#request get method url: "/"

my_posts = [{"title":"title of post 1", "content":"content of post 1", "id":1},
            {"title":"favourite foods", "content" : "i like pizzaa", "id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id']  == id:
            return i

@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_post(body:dict = Body(...)):
def create_posts(post:Post):
    # print(post.rating)
    post_dict = post.dict()
    print(post.dict()) #to convert into dictionary
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return{"data":post_dict}
    # return {"new_posts":f"title {body['title']} content: {body['content']}"}
#title str, content str, category, bool published post


@app.get("/posts/latest")                           #this is for reference that fast api matches the first path
def get_latest_post():                                #this will throw error if after {id} parameter
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

@app.get("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)          #the parameter is always returned as string , dont forget to convert it back
def get_post(id: int, response:Response):
    # print(type(id))
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail =f'post with id: {id} was not found' )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message':f'post with id: {id} was not found'}
    return{"post_detail": post}



@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    #deleting post
    #find the index in the array that has required ID 
    #my_posts.pop(index)\
    index = find_index_post(id)
    
    if index == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"post with id:{id} does not exist")
    
    my_posts.pop(index)
    return Response (status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int, post:Post):
    index = find_index_post(id)
        
    if index == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"post with id:{id} does not exist")
        
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return{'data':post_dict}
 
