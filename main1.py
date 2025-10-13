# from fastapi import FastAPI, Response, status, HTTPException, Depends
# from pydantic import BaseModel
# from fastapi.params import Body
# from typing import Optional, List
# import passlib

# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
# import utils
# from sqlalchemy.orm import Session
# import models
# from database import engine, get_db
# from models import Base
# import schemas
# from utils import hash

# from routers import post, user, auth
# import oauth2

# # Base.metadata.drop_all(bind=engine)   # drops all tables
# # Create tables
# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# my_posts = [
#     {"title":"title of post 1", "content":"content of post 1", "id":1},
#     {"title":"favourite foods", "content":"i like pizzaa", "id":2}
# ]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i

# app.include_router(post.router)
# app.include_router(user.router)
# app.include_router(auth.router)

# @app.get("/")
# def root():
#     return {"message":"hello world"}


from fastapi import FastAPI
from sqlalchemy.orm import Session
import models
from database import engine
from routers import post, user, auth

# Create tables if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello, world! FastAPI backend is running 🚀"}
