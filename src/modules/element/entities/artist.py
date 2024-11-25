
# Artist Model
from pydantic import BaseModel
from typing import Optional

class Artist(BaseModel):
    id: Optional[str]
    name: str
    age: int
    country: str