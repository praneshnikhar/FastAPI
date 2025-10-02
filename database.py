# creating a database 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:pranesh@localhost/fastapi2'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)


Base = declarative_base()
 
# to get the database connection/session dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()