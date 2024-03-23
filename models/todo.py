from pydantic import BaseModel,Field


class Todo(BaseModel):
    id:str = Field(alias="_id")
    title: str
    description: str
    isComplete: bool
    createdAt: str
    updatedAt: str
    