from fastapi import Depends, APIRouter, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schema import GetPost, CreatePost, UpdatePost
from ..db_init import get_db
from ..db.models import Post

router = APIRouter()
    
@router.get("/posts", response_model= List[GetPost])
async def get_all_posts(db: Session = Depends(get_db)):
    
    all_posts =  db.query(Post).all()
    
    if not all_posts: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No Posts Found")
        
    return all_posts

@router.get("/post/{post_id}")
async def get_post(post_id: int, db: Session = Depends(get_db)):
    
    single_post =  db.query(Post).filter(Post.id == post_id).first()
    
    if not single_post: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post Not Found")
    
    return single_post

@router.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(create_post: CreatePost, db: Session = Depends(get_db)):

    new_post = Post(**create_post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    
    post =  db.query(Post).filter(Post.id == post_id)
    
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post {post_id} does not exist")
        
    post.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/posts/{post_id}")
async def update_post(post_id: int, update_post: UpdatePost, db: Session = Depends(get_db)):
    
    post_query =  db.query(Post).filter(Post.id == post_id)
    
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post {post_id} does not exist")
        
    post_query.update(update_post.dict(), synchronize_session=False)
    db.commit()
    
    return post_query.first()