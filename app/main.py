from fastapi import FastAPI
from .api import users, posts
# import db_init
from .db import models
from .db_init import SessionLocal, Base, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(posts.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
