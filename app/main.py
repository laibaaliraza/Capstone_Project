from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI app running inside Docker!"}

@app.get("/tasks")
def read_tasks():
    return {"message": "Tasks endpoint working!"}
