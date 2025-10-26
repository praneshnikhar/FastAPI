from fastapi import FastAPI
from sqlalchemy.orm import Session
import models
from database import engine
from routers import post, user, auth
from config import settings  

print(settings.database_password)
print(settings.database_path)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello, world! FastAPI backend is running 🚀"}
