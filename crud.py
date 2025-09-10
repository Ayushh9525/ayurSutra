from sqlalchemy.orm import Session
import models, schemas

def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    db_appointment = models.Appointment(
        patient_name=appointment.patient_name,
        therapy_name=appointment.therapy_name,
        date_time=appointment.date_time,
        status="scheduled"
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def get_appointments(db: Session):
    return db.query(models.Appointment).all()
