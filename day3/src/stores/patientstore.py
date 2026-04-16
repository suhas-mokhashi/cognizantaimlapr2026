""""create patient store to manage patient data
"""
class PatientStore:
    def __init__(self):
        self.patients={}

    def add_patient(self, patient):
        self.patients[patient.id]=patient

    def get_all_patients(self):
        return list(self.patients.values()) 
    
    def get_patient_by_id(self, patient_id):
        for patient in self.patients.values():
            if patient.id == patient_id:
                return patient
        raise PatientNotFoundException(f"Patient with id {patient_id} not found")

    def update_patient(self, patient_id, name=None, dob=None, ailment=None):
        patient=self.get_patient_by_id(patient_id)
        if name:
            patient.name=name
        if dob:
            patient.dob=dob
        if ailment:
            patient.ailment=ailment