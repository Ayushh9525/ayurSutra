from pydantic import BaseModel
import datetime

class AppointmentCreate(BaseModel):
    patient_name: str
    therapy_name: str
    date_time: datetime.datetime

class Appointment(AppointmentCreate):
    id: int
    status: str

    class Config:
        from_attributes = True
