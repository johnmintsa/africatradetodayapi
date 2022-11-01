from email import message
from optparse import Option
from turtle import pos

from app.models import models 
from app.schema import schemas
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app.database.database import get_db, SessionLocal, engine
from typing import Optional, List
from oauth2.oauth2 import get_current_user


router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db:Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {vote.post_id} does not exist")

    vote_query = db.query(models.vote).filter(models.vote.post_id == vote.post_id)
    found_vote = vote_query.first()

    if(vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} has already voted on post {vote.post_id}")
            
        new_vote = models.vote(post_id = vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()

        return {"message":"successfully added vote"}
    else:

        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exists")
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message":"Successfully deleted vote"}
