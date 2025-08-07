from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.team_capstone import TeamCapstone
from app.schemas.team_capstone import TeamCapstoneCreate, TeamCapstoneResponse
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks/", response_model=TeamCapstoneResponse)
def create_task(task: TeamCapstoneCreate, db: Session = Depends(get_db)):
    db_task = TeamCapstone(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/tasks/", response_model=list[TeamCapstoneResponse])
def read_tasks(db: Session = Depends(get_db)):
    return db.query(TeamCapstone).all()
