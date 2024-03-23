from pydantic import BaseModel
from models import todo

class One_Todo(BaseModel):
    statusCode:int
    message:str
    data: todo.Todo
    success:bool