from pydantic import BaseModel

class TeamCapstoneBase(BaseModel):
    title: str
    description: str

class TeamCapstoneCreate(TeamCapstoneBase):
    pass

class TeamCapstoneResponse(TeamCapstoneBase):
    id: int

    class Config:
        orm_mode = True
