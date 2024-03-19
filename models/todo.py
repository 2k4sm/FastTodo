from pydantic import BaseModel,Field


class Todo(BaseModel):
    id:str = Field(alias="_id")
    description:str
    title: str
    isComplete:bool
    updatedAt:str
    