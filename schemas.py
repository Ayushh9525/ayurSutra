# from pydantic import BaseModel
# import datetime

# class AppointmentCreate(BaseModel):
#     patient_name: str
#     therapy_name: str
#     date_time: datetime.datetime

# class Appointment(AppointmentCreate):
#     id: int
#     status: str

#     class Config:
#         from_attributes = True






from pydantic import BaseModel
import datetime

# ---------------- Patients -----------------
class PatientCreate(BaseModel):
    name: str
    email: str
    phone: str | None = None

class Patient(PatientCreate):
    id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True


# ---------------- Practitioners -----------------
class PractitionerCreate(BaseModel):
    name: str
    specialization: str | None = None
    email: str
    phone: str | None = None

class Practitioner(PractitionerCreate):
    id: int

    class Config:
        from_attributes = True


# ---------------- Appointments -----------------
class AppointmentCreate(BaseModel):
    patient_id: int
    practitioner_id: int
    therapy_name: str
    date_time: datetime.datetime

class Appointment(AppointmentCreate):
    id: int
    status: str

    class Config:
        from_attributes = True
