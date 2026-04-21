#create full name class
class FullName:
    def __init__(self, first_name: str, last_name: str):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self) -> str:
        return self.__first_name
    @first_name.setter
    def first_name(self, value: str):
        if not value:
            raise ValueError("First name cannot be empty")
        self.__first_name = value
    @property
    def last_name(self) -> str:
        return self.__last_name
    @last_name.setter
    def last_name(self, value: str):        
        if not value:
            raise ValueError("Last name cannot be empty")
        self.__last_name = value