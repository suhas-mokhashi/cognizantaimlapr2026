"""
create doctor store to manage doctor data
"""
import sys
import os 
from exceptions.doctor_not_found_exception import DoctorNotFoundException
from models.doctor import Doctor

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from configuration.logger_conf import setup_logger
logger = setup_logger()


class DoctorStore:
    def __init__(self):
        self.doctors={}

    def add_doctor(self, doctor: Doctor):
        self.doctors[doctor.id]=doctor
        logger.info(f"Added doctor: {doctor}")

    def delete_doctor(self, doctor_id: int):
        if doctor_id in self.doctors:
            del self.doctors[doctor_id]
            logger.info(f"Deleted doctor with id {doctor_id}")
        else:
            raise DoctorNotFoundException(f"Doctor with id {doctor_id} not found")

    def get_all_doctors(self):
        return list(self.doctors.values())
        logger.info("Retrieved all doctors")


    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        for doctor in self.doctors.values():
            if doctor.id == doctor_id:
                return doctor
        raise DoctorNotFoundException(f"Doctor with id {doctor_id} not found")

    def update_doctor(self, doctor_id: int, name: str = None, specialization: str = None):
        doctor=self.get_doctor_by_id(doctor_id)
        logger.info(f"Updating doctor with id {doctor_id}")
        if name:
            doctor.name=name
        if specialization:
            doctor.specialization=specialization
