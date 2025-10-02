from sqlalchemy import Column, Integer, String, Boolean
from database import Base 
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    cintent= Column(String, nullable = False)
    published = Column(Boolean, server_default='TRUE', nullable = False)
    created_at = Column(TIMESTAMP(timezone = True), nullable= False, server_default=text('now()'))
    

class Blog(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)
 
 