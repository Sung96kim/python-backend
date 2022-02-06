import fastapi
from typing import Optional

router = fastapi.APIRouter()

@router.get("/users")
async def get_users():
    return {"Hello": "World"}

@router.get("/user/{user_id}")
async def get_user(user_id: int, q: Optional[str] = None):
    return {"user_id": user_id, "q": q}

