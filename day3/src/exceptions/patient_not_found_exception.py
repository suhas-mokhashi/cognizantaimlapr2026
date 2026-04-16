"""
patient not found exception
"""
class PatientNotFoundException(Exception):
    """exception to be raised when patient is not found
    """
    def __init__(self, message="Patient not found"):
        self.message=message
        super().__init__(self.message)