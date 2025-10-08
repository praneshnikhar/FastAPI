from fastapi import APIRouter , Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(tags = ['Authentication'])
import database, schemas, models, utils, oauth2

@router.post('/login')
def login(user_credentials:OAuth2PasswordRequestForm= Depends(), db:Session= Depends(database.get_db)):
    # {
    #     "username": "asdf ",
    #     "password" : "alsdjf"
    # }
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"invalid credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"invalid credentials")
    
    access_token = oauth2.create_access_token(data = {"user_id":user.id})
    
    #create a token , then return token 
    return {"access_token": access_token, "token_type": "bearer"}

    