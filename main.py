from fastapi import FastAPI
from datetime import datetime
import requests
from models import all_todos,create_todo,todos

fastTodo = FastAPI()
@fastTodo.get("/")
async def root():
    return {"message":"API is running.....","time": datetime.now()}

@fastTodo.get("/todos")
async def getAllTodos():
    resp = requests.get("https://api.freeapi.app/api/v1/todos")
    
    resp_json = resp.json()
    
    alltodos = all_todos.ListTodo.parse_obj(resp_json)
    
    return alltodos


@fastTodo.get("/todos/{todoId}")
async def getTodoById(todoId : str):
    resp = requests.get("https://api.freeapi.app/api/v1/todos/"+todoId)
    
    resp_json = resp.json()
    
    todo = todos.One_Todo.parse_obj(resp_json)
    
    return todo

@fastTodo.delete("/todos/{todoId}")
async def deleteTodo(todoId : str):
    
    resp = requests.delete("https://api.freeapi.app/api/v1/todos/"+todoId)
    
    resp_json = resp.json()
    
    return {"status":resp.status_code,"message":resp_json["message"]}

@fastTodo.patch("/todos/{todoId}")
async def createTodo(todoId : str,todo :create_todo.CreateTodo):
    
    resp = requests.patch(url="https://api.freeapi.app/api/v1/todos/"+todoId,data=todo.dict())
    
    resp_json = resp.json()
    
    todo = todos.One_Todo.parse_obj(resp_json)
    
    return todo

@fastTodo.patch("/todos/toggle/status/{todoId}")
async def updateTodo(todoId : str):
    resp = requests.patch("https://api.freeapi.app/api/v1/todos/toggle/status/"+todoId)
    
    resp_json = resp.json()
    
    todo = todos.One_Todo.parse_obj(resp_json)
    
    return todo

@fastTodo.post("/todos/")
async def createTodo(todo:create_todo.CreateTodo):
    
    resp = requests.post(url="https://api.freeapi.app/api/v1/todos/",data=todo.dict())
    
    resp_json = resp.json()
    
    todo = todos.One_Todo.parse_obj(resp_json)
    
    return todo