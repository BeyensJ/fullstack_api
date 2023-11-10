from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import app.crud as crud
import app.models as models
import app.schemas as schemas
from fastapi.middleware.cors import CORSMiddleware
from app.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to jitse's FastAPI!"}
