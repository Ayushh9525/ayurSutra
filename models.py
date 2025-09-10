from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String, index=True)
    therapy_name = Column(String, index=True)
    date_time = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default="scheduled")
