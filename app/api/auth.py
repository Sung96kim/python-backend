from ctypes import util
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import db_init, schema, utils, oauth
from ..db.models import User

router = APIRouter(
    tags=["Authentication"]
)

@router.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(db_init.get_db)):
    
    user = db.query(User).filter(User.email == user_credentials.username).first()
    
    if not user: 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail=f"Invalid Login Credentials")
        
    if not utils.verify_pwd(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail=f"Invalid Login Credentials")
    
    # data in params is where you would add more information related to the user
    access_token = oauth.create_access_token(data = {"user_id": user.id})
    
    return {"access_token": access_token, "token_type": "bearer"}