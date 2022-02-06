from .db.models import User
from .schema import CreateUser
from sqlalchemy.orm import Session
from fastapi import Depends
from .db_init import get_db

async def seed_database(db: Session = Depends(get_db)):
    users = [
        {
            "email": "sung96kim@gmail.com",
            "password": "password"
        },
        {
            "email": "sung123kim@gmail.com",
            "password": "password"
        }
    ]
    
    for user in users:
        modeledUser = CreateUser(user)
        seedUser = User(modeledUser)
        await db.add(seedUser)
        await db.commit()
    
    print("Users Seeded!")
