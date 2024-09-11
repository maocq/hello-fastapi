from pydantic import BaseModel

class User(BaseModel):
    id: int = 0
    name: str
    description: str | None = None