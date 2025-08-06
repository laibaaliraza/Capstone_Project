from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()
get_db = database.get_db

@router.post("/", response_model=schemas.TeamCapstone)
def create_team_capstone(request: schemas.TeamCapstoneCreate, db: Session = Depends(get_db)):
    new_entry = models.TeamCapstone(title=request.title, description=request.description)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry
