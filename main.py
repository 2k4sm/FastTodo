from fastapi import FastAPI
from datetime import datetime
import requests
from models import list_todo
app = FastAPI()


@app.get("/")
async def root():
    return {"message": datetime.now()}

@app.get("/todos")
async def getAllTodos():
    resp = requests.get("https://api.freeapi.app/api/v1/todos")
    
    resp_json = resp.json()
    
    alltodos = list_todo.ListTodo.parse_obj(resp_json)
    
    return alltodos
