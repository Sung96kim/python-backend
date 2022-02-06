from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .api import users, posts
from .db import models
from .db_init import engine, get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(posts.router)

# @app.get("/")
# def root(db: Session = Depends(get_db)):
#     return "Database Active"

    