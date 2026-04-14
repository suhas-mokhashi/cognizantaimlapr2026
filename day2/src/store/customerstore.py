#generate 100 customers and store in a list
import typing
import faker
from models.customer import Customer
class CustomerStore:
    def __init__(self,num_customers:int):
        self.customers = []
        self.generate_customers(num_customers)
        

    def generate_customers(self, num_customers:int):
        self.fake = faker.Faker()
        for _ in range(num_customers):
            name = self.fake.name()
            email = self.fake.email()
            dob = self.fake.date_of_birth()
            customer = Customer(name, email, dob)
            self.customers.append(customer)

    def get_customers(self)->typing.List[Customer]:
        return self.customers