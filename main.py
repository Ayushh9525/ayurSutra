# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from database import engine, SessionLocal, Base
# import models, schemas, crud

# # Create tables
# Base.metadata.create_all(bind=engine)

# app = FastAPI(title="AyurSutra Backend 🚑")

# # Dependency to get DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get("/")
# def root():
#     return {"message": "AyurSutra Backend is running 🚀"}

# # --------------------
# # Appointments APIs
# # --------------------
# @app.post("/appointments/", response_model=schemas.Appointment)
# def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
#     return crud.create_appointment(db, appointment)

# @app.get("/appointments/", response_model=list[schemas.Appointment])
# def list_appointments(db: Session = Depends(get_db)):
#     return crud.get_appointments(db)




# from fastapi import BackgroundTasks, Depends, FastAPI
# from sqlalchemy.orm import Session
# import crud, schemas
# from database import SessionLocal, engine
# from notifications import send_email
# from fastapi import FastAPI

# app = FastAPI()

# # Dependency to get DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()




# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Backend is running!"}




# @app.post("/appointments/", response_model=schemas.Appointment)
# async def create_appointment(
#     appointment: schemas.AppointmentCreate,
#     background_tasks: BackgroundTasks,
#     db: Session = Depends(get_db)
# ):
#     db_appointment = crud.create_appointment(db, appointment)

#     # TODO: Fetch patient email from DB (right now hardcoded for testing)
#     background_tasks.add_task(
#         send_email,
#         subject="Appointment Scheduled",
#         email_to="patient@gmail.com",
#         body=f"Dear {appointment.patient_name}, your therapy {appointment.therapy_name} is scheduled on {appointment.date_time}"
#     )

#     return db_appointment



# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Backend running ✅"}


from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------- Patients --------
@app.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db, patient)

@app.get("/patients/", response_model=list[schemas.Patient])
def read_patients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_patients(db, skip=skip, limit=limit)


# -------- Practitioners --------
@app.post("/practitioners/", response_model=schemas.Practitioner)
def create_practitioner(practitioner: schemas.PractitionerCreate, db: Session = Depends(get_db)):
    return crud.create_practitioner(db, practitioner)

@app.get("/practitioners/", response_model=list[schemas.Practitioner])
def read_practitioners(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_practitioners(db, skip=skip, limit=limit)


# -------- Appointments --------
@app.post("/appointments/", response_model=schemas.Appointment)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    return crud.create_appointment(db, appointment)

@app.get("/appointments/", response_model=list[schemas.Appointment])
def read_appointments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_appointments(db, skip=skip, limit=limit)
