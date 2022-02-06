from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String
from ..db_init import Base
from sqlalchemy.orm import relationship
from sqlalchemy import *

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    email= Column(String, unique=True, index=True, nullable=False)
    password= Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    # posts = relationship("Post", back_populates="user")
    #Add uselist=False when creating a one to one relationship, since one to many is default
    # posts = relationship("Post", back_populates="user", userlist=False)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    # user_id = Column(Integer, ForeignKey("users.id"))
    # owner = relationship("User", back_populates="post")
