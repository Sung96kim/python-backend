from http.client import HTTPException
from fastapi import Depends, APIRouter, status, Response
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ..db_init import get_db
from ..db.models import Post

router = APIRouter()

class Post(BaseModel):
    title: str
    author: str
    content: str
    
@router.get("/posts")
async def get_all_posts(db: Session = Depends(get_db)):
    
    all_posts = db.query(Post).all()
    return { "All Posts:" : all_posts }

@router.get("/post/{post_id}")
async def get_post(post_id: int, db: Session = Depends(get_db)):
    
    single_post = db.query(Post).filter(Post.id == post_id).first()
    return { "Selected Post" : single_post }

@router.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(create_post: Post, db: Session = Depends(get_db)):

    new_post = Post(**create_post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return { "data": new_post}

@router.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    
    post = db.query(Post).filter(Post.id == post_id)
    
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post {post_id} does not exist")
        
    post.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/posts/{post_id}")
async def update_post(post_id: int, update_post: Post, db: Session = Depends(get_db)):
    
    post_query = db.query(Post).filter(Post.id == post_id)
    
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post {post_id} does not exist")
        
    post_query.update(update_post.dict(), synchronize_session=False)
    db.commit()
    
    return { "data": post_query.first()}