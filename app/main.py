
from fastapi import FastAPI
from app.middleware import LoggingMiddleware
from app.routers import team_capstone
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(LoggingMiddleware)

@app.get("/")
def read_root():
    return {"message": "Welcome to Team Capstone API", "endpoints": ["/tasks/"]}

app.include_router(team_capstone.router)