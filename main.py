from fastapi import FastAPI
from api import users, posts
import db_init
from models import models

app = FastAPI()

models.Base.metadata.create_all(bind=db_init.engine)

app.include_router(users.router)
app.include_router(posts.router)
