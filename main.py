from fastapi import FastAPI
from typing import Optional
app = FastAPI()

# @app.get('/blog?limit=10&published= true')
# def index():
#     return {'data':{'name' : 'pranesh'}} 

@app.get('/blog')
def index(limit = 10, published:bool = True, sort: Optional[str]= None):
    #if u put 10 in url. , then only get 10 published blogs
    # return published
    
    if published: 
        return {'data':f'{limit} published blogs from the db'} 
    else:
        return {'data':f'{limit} blogs from the db'} 

@app.get('/about')
def about():
    return {'data':'about page'}
 ######################################
@app.get('/blog/{id}')
def show(id:str):
    #fetch blog with id = id 
    return {'data':id}                  
                                    #check routing here , in earlier version ,it would go line by lune
                                    # and the add 'unpublished' word in id , in show method , in this version of 
                                    #fast api it would do it perfectly if it matches wit the word unpublished
@app.get('blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}
###########################################

@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    #fetch comments of blog with id = id
    return limit
    return {'data':{'1', '2'}}

#use- python -m uvicorn main:app --reload
#localhost:8000/docs
#localhost:8000/redoc
