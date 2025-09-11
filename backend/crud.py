# from sqlalchemy.orm import Session
# import models, schemas

# def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
#     db_appointment = models.Appointment(
#         patient_name=appointment.patient_name,
#         therapy_name=appointment.therapy_name,
#         date_time=appointment.date_time,
#         status="scheduled"
#     )
#     db.add(db_appointment)
#     db.commit()
#     db.refresh(db_appointment)
#     return db_appointment

# def get_appointments(db: Session):
#     return db.query(models.Appointment).all()



# from sqlalchemy.orm import Session
# import models, schemas

# # ---------- Patients ----------
# def create_patient(db: Session, patient: schemas.PatientCreate):
#     db_patient = models.Patient(**patient.dict())
#     db.add(db_patient)
#     db.commit()
#     db.refresh(db_patient)
#     return db_patient

# def get_patients(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(models.Patient).offset(skip).limit(limit).all()


# # ---------- Practitioners ----------
# def create_practitioner(db: Session, practitioner: schemas.PractitionerCreate):
#     db_practitioner = models.Practitioner(**practitioner.dict())
#     db.add(db_practitioner)
#     db.commit()
#     db.refresh(db_practitioner)
#     return db_practitioner

# def get_practitioners(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(models.Practitioner).offset(skip).limit(limit).all()


# # ---------- Appointments ----------
# def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
#     db_appointment = models.Appointment(**appointment.dict())
#     db.add(db_appointment)
#     db.commit()
#     db.refresh(db_appointment)
#     return db_appointment

# def get_appointments(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(models.Appointment).offset(skip).limit(limit).all()


from sqlalchemy.orm import Session
import models, schemas

# ---------- Patients ----------
def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patients(db: Session):
    return db.query(models.Patient).all()


# ---------- Practitioners ----------
def create_practitioner(db: Session, practitioner: schemas.PractitionerCreate):
    db_practitioner = models.Practitioner(**practitioner.dict())
    db.add(db_practitioner)
    db.commit()
    db.refresh(db_practitioner)
    return db_practitioner

def get_practitioners(db: Session):
    return db.query(models.Practitioner).all()


# ---------- Appointments ----------
def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    db_appointment = models.Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def get_appointments(db: Session):
    return db.query(models.Appointment).all()
