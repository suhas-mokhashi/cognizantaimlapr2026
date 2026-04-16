"""create appointment with id patient doctor date and time
"""
from datetime import date, time
from patient import Patient
from doctor import Doctor
class Appointment:
    def __init__(self,id: int, patient: Patient, doctor: Doctor, date: date, time: time):
        self.appointment_id=id
        self.patient=patient    
        self.doctor=doctor
        self.date=date
        self.time=time

    def __str__(self):
        return f"Appointment(id={self.appointment_id}, patient={self.patient}, doctor={self.doctor}, date={self.date}, time={self.time})"