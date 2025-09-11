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






# from pydantic import BaseModel
# import datetime

# # ---------------- Patients -----------------
# class PatientCreate(BaseModel):
#     name: str
#     email: str
#     phone: str | None = None

# class Patient(PatientCreate):
#     id: int
#     created_at: datetime.datetime

#     class Config:
#         from_attributes = True


# # ---------------- Practitioners -----------------
# class PractitionerCreate(BaseModel):
#     name: str
#     specialization: str | None = None
#     email: str
#     phone: str | None = None

# class Practitioner(PractitionerCreate):
#     id: int

#     class Config:
#         from_attributes = True


# # ---------------- Appointments -----------------
# class AppointmentCreate(BaseModel):
#     patient_id: int
#     practitioner_id: int
#     therapy_name: str
#     date_time: datetime.datetime

# class Appointment(AppointmentCreate):
#     id: int
#     status: str

#     class Config:
#         from_attributes = True





from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ---------- Patient ----------
class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    email: str
    phone: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True


# ---------- Practitioner ----------
class PractitionerBase(BaseModel):
    name: str
    specialization: str
    email: str

class PractitionerCreate(PractitionerBase):
    pass

class Practitioner(PractitionerBase):
    id: int

    class Config:
        orm_mode = True


# ---------- Appointment ----------
class AppointmentBase(BaseModel):
    patient_id: int
    practitioner_id: int
    therapy_type: str
    scheduled_time: Optional[datetime] = None

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int

    class Config:
        orm_mode = True
