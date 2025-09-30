from fastapi import FastAPI
from fastapi.params import Body, BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

#request get method url: "/"

@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "this is your posts"}

@app.post("/createposts")
# def create_post(body:dict = Body(...)):
def create_posts(new_post:Post):
    print(new_post)
    return{"data":"new posts"}
    # return {"new_posts":f"title {body['title']} content: {body['content']}"}
#title str, content str, category, bool published post
