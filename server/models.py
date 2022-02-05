from turtle import back
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text
from .db import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username= Column(String)
    email= Column(String, unique=True, index=True)
    password= Column(String)

    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    content = Column(Text)

    owner = relationship("User", back_populates="posts")



    def __repr__(self):
        return "<Post(title='{}', author='{}', content={})>"\
                .format(self.title, self.author, self.content)

    

