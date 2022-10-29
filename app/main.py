from fastapi import FastAPI
from models import models
from router import post,users, auth, vote
from database import database
from config.config import Settings
from fastapi.middleware.cors import CORSMiddleware






#models.Base.metadata.create_all(bind=database.engine)



app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



 




app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)