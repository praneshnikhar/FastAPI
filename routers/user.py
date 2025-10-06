from fastapi import status, HTTPException, Depends, APIRouter
from random import randrange
import utils
from sqlalchemy.orm import Session
import models
from database import engine, get_db
from database import engine
from models import Base
import schemas

router=APIRouter(
    prefix = "/users"
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model = schemas.UserOut)
def create_user(user:schemas.UserCreate, db:Session= Depends(get_db)): 
    
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.get('/{id}',response_model = schemas.UserOut)
def get_user(id: int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"user with id: {id} does not exist") 
    return user
