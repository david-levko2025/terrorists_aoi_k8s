from pydantic import BaseModel


class Terorists(BaseModel):
    
    name : str
    danger_rate : int
    location : str
