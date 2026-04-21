#create customer model

from src.models.full_name import FullName


class Customer:
    def __init__(self, customer_id: int, full_name: FullName, email: str, phone_no: int):
        #protected attributes
        self._customer_id = customer_id
        self._full_name = full_name
        self._email = email
        self._phone_no = phone_no
    #getters and setters
    @property
    def customer_id(self):
        return self._customer_id    
    @customer_id.setter
    def customer_id(self, customer_id):
        self._customer_id = customer_id
    @property
    def full_name(self):
        return self._full_name
    @full_name.setter
    def full_name(self, full_name):
        self._full_name = full_name
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email
    @property
    def phone_no(self):
        return self._phone_no
    @phone_no.setter
    def phone_no(self, phone_no):
        self._phone_no = phone_no