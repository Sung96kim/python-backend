from fastapi import FastAPI
from .api import users, posts, auth
from .db import models
from .db_init import engine
# from .config import settings

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router)

    