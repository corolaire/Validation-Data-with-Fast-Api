from pydantic import BaseModel,Field
from typing import Optional

class user(BaseModel):
    id_user:Optional[str]=None
    name:str=Field(min_length=2,max_length=12,nullable=False)
    email:str=Field(min_length=4,max_length=100,nullable=False)
    password:str=Field(min_length=1,max_length=20,nullable=False)
    