
from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List
from random import randrange
from sqlalchemy.orm import Session
import models
from database import engine, get_db
from database import engine
from models import Base
import schemas

router = APIRouter(
    prefix = "/posts", #+ #/{id}.
    tags=['Posts']
)

@router.get("/", response_model =List[schemas.Post])
def get_posts(db:Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model = schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    
    new_post = models.Post(**post.dict(exclude={"rating"}))
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post

# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[-1]
#     return {"detail": post}

@router.get("/{id}", response_model = schemas.Post)
def get_post(id: int, db:Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with id: {id} was not found'
        )
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db:Session = Depends(get_db)):
    index = find_index_post(id)
    # if index is None:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"post with id:{id} does not exist"
    #     )
    # my_posts.pop(index)
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} does not exist")
    post.delete(synchronize_session = False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model = schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate):
    # index = find_index_post(id)
    # if index is None:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"post with id:{id} does not exist"
    #      )
    # post_dict = post.dict()
    # post_dict['id'] = id
    # my_posts[index] = post_dict
    # return {'data': post_dict}
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    if post ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id :{id} does not exist")
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    
    db.commit()
    
    return post_query.first()
