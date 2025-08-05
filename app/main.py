#API endpoints eg get tasks etc
from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/tasks")
def read_tasks():
    return {"message": "Tasks endpoint working!"}
