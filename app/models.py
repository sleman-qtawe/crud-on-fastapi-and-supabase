from pydantic import BaseModel
from datetime import datetime

class Appointment(BaseModel):
    name: str
    id_number: str
    specialization: str
    datetime: datetime