# from sqlalchemy import Column, Integer, String, DateTime
# from database import Base
# import datetime

# class Appointment(Base):
#     __tablename__ = "appointments"

#     id = Column(Integer, primary_key=True, index=True)
#     patient_name = Column(String, index=True)
#     therapy_name = Column(String, index=True)
#     date_time = Column(DateTime, default=datetime.datetime.utcnow)
#     status = Column(String, default="scheduled")





# *****************************************************************************************B 


# from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
# from sqlalchemy.orm import relationship
# from database import Base
# import datetime

# class Patient(Base):
#     __tablename__ = "patients"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     email = Column(String, unique=True, index=True, nullable=False)
#     phone = Column(String, nullable=True)
#     created_at = Column(DateTime, default=datetime.datetime.utcnow)

#     appointments = relationship("Appointment", back_populates="patient")


# class Practitioner(Base):
#     __tablename__ = "practitioners"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     specialization = Column(String, nullable=True)
#     email = Column(String, unique=True, index=True, nullable=False)
#     phone = Column(String, nullable=True)

#     appointments = relationship("Appointment", back_populates="practitioner")


# class Appointment(Base):
#     __tablename__ = "appointments"

#     id = Column(Integer, primary_key=True, index=True)
#     patient_id = Column(Integer, ForeignKey("patients.id"))
#     practitioner_id = Column(Integer, ForeignKey("practitioners.id"))
#     therapy_name = Column(String, nullable=False)
#     date_time = Column(DateTime, nullable=False)
#     status = Column(String, default="Scheduled")

#     patient = relationship("Patient", back_populates="appointments")
#     practitioner = relationship("Practitioner", back_populates="appointments")








from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)

    appointments = relationship("Appointment", back_populates="patient")


class Practitioner(Base):
    __tablename__ = "practitioners"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    specialization = Column(String)
    email = Column(String, unique=True, index=True)

    appointments = relationship("Appointment", back_populates="practitioner")


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    practitioner_id = Column(Integer, ForeignKey("practitioners.id"))
    therapy_type = Column(String)
    scheduled_time = Column(DateTime, default=datetime.datetime.utcnow)

    patient = relationship("Patient", back_populates="appointments")
    practitioner = relationship("Practitioner", back_populates="appointments")
