import fastapi

router = fastapi.APIRouter()

@router.get("/posts/{post_id}")
async def get_post(post_id: int):
    return {"Post ID:" : post_id}

@router.post("/posts")
async def add_post(post: str):
    return {"Post:" : post}
