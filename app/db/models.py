from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text
from ..db_init import Base
from sqlalchemy.orm import relationship
from sqlalchemy import *

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username= Column(String)
    email= Column(String, unique=True, index=True, nullable=False)
    password= Column(String)
    posts = relationship("Post", back_populates="user")

    #Add uselist=False when creating a one to one relationship, since one to many is default
    # posts = relationship("Post", back_populates="user", userlist=False)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="post")

    def __repr__(self):
        return "<Post(title='{}', author='{}', content={})>"\
                .format(self.title, self.author, self.content)
