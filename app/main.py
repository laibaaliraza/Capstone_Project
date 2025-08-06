from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import team_capstone
from .database import engine
from . import models

# Create all database tables
models.Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI(
    title="Capstone Project API",
    version="1.0.0"
)

# Enable CORS (important if you're using this from a frontend like React or Vue)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your router with a proper prefix
app.include_router(team_capstone.router, prefix="/api/team_capstone", tags=["Team Capstone"])


# Health check or root route
@app.get("/")
def read_root():
    return {"msg": "Hello from FastAPI!"}
