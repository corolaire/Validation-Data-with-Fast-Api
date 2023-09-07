from pydantic import BaseModel,Field
from typing import Optional

class profile (BaseModel):
    id_profile:Optional[str]=None
    name:str=Field(min_length=2,max_length=12,nullable=False)
    lastname:str=Field(min_length=2,max_length=15,nullable=False)
    phonenumber:int=Field(min_length=10,max_length=1,nullable=False)
    age:int=Field(ge=18,lt=100,nullable=False)
    gender:str=Field(min_length=2,max_length=20,nullable=False)