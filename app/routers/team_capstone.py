from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/team_capstone",
    tags=["Team Capstone"]
)

# Example schema
class TeamMember(BaseModel):
    name: str
    role: str
    email: str

# Dummy database (in-memory list for example)
team_members = [
    {"name": "Laiba", "role": "DevOps Engineer", "email": "laiba@example.com"},
    {"name": "Ahmed", "role": "Backend Developer", "email": "ahmed@example.com"}
]

# GET endpoint to return all team members
@router.get("/", response_model=List[TeamMember])
async def get_team_members():
    return team_members

# POST endpoint to add a new team member
@router.post("/", response_model=TeamMember)
async def add_team_member(member: TeamMember):
    team_members.append(member.dict())
    return member
