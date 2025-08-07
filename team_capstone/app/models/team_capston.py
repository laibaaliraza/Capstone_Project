from sqlalchemy import Column, Integer, String
from ..database import Base

class TeamCapstone(Base):
    __tablename__ = "team_capstone"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
