from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from ..schema import GetUser, CreateUser, UpdateUser
from ..db_init import get_db
from ..db.models import User

router = APIRouter()

@router.get("/user/{user_id}", response_model= GetUser)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    
    user = db.query(User).filter(User.id == user_id).first()
    
    if user == None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User Not Found")
        
    return user

@router.post("/user")
async def create_user(user: CreateUser, db: Session = Depends(get_db)):
    
    created_user = User(**user.dict())
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    
    if not created_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User could not be created")
    
    return created_user

@router.put("/user/{user_id}")
async def update_user(user_id: int, update_user: UpdateUser, db: Session = Depends(get_db)):
    
    found_user = db.query(User).filter(User.id == user_id)
    
    user = found_user.first()
    
    if user == None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User does not exist")

    found_user.update(update_user.dict(), synchronize_session=False)
    db.commit()
    
    return found_user.first()