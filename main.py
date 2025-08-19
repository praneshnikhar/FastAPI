from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name' : 'pranesh'}} 

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
def comments(id):
    #fetch comments of blog with id = id
    return {'data':{'1', '2'}}