"""create doctor not found exception to handle doctor not found error
"""
class DoctorNotFoundException(Exception):
    """exception to be raised when doctor is not found
    """
    def __init__(self, message="Doctor not found"):
        self.message=message
        super().__init__(self.message)