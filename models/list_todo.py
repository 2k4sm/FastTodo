from pydantic import BaseModel
from models import todo
class ListTodo(BaseModel):
    statusCode:int
    message:str
    data:list[todo.Todo]
    success:bool