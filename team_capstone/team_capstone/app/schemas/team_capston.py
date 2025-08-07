from pydantic import BaseModel

class TeamCapstoneCreate(BaseModel):
    title: str
    description: str

class TeamCapstone(TeamCapstoneCreate):
    id: int

    class Config:
        orm_mode = True
