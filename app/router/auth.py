

from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app.database import database
from app.schema import schemas
from app.models import models
from app.util import util
from app.oauth2 import oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Authentication']
    )

@router.post('/login', response_model= schemas.Token)
def login(user_creditentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_creditentials.username).first()

    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not util.verify(user_creditentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,  detail=f"Invalid Creditentials")
    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    # create a token 
    # return toekn 
    return {"access_token":access_token, "token_type":"bearer"}
