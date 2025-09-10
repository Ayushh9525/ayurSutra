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




from fastapi import BackgroundTasks, Depends, FastAPI
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionLocal, engine
from notifications import send_email
from fastapi import FastAPI

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend is running!"}




@app.post("/appointments/", response_model=schemas.Appointment)
async def create_appointment(
    appointment: schemas.AppointmentCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    db_appointment = crud.create_appointment(db, appointment)

    # TODO: Fetch patient email from DB (right now hardcoded for testing)
    background_tasks.add_task(
        send_email,
        subject="Appointment Scheduled",
        email_to="patient@gmail.com",
        body=f"Dear {appointment.patient_name}, your therapy {appointment.therapy_name} is scheduled on {appointment.date_time}"
    )

    return db_appointment
