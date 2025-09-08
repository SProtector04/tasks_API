from fastapi import FastAPI

# FastAPI instance
app = FastAPI(title="Tasks API", version="0.0.1")

# Health-checking the route
@app.get("/")
def read_root():
    return {"message": "Tasks API is running 🚀"}

# Example placeholder endpoint
@app.get("/tasks")
def get_tasks():
    return [{"id": 1, "title": "First Task", "done": False}]
