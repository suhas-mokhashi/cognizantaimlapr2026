import pandas as pd
import sys
import os

# Add project root to Python path for Banking imports
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)

from src.models.full_name import FullName
from src.data_loader.customer_data_loader import CustomerDataLoader
from src.models.customer import Customer
from src.stores.customer_store_impl import CustomerStoreImpl
class CustomerCSVDataLoader(CustomerDataLoader):
    def load_data(self, file_path, customer_store:CustomerStoreImpl):
        data=pd.read_csv(file_path)
        for _, row in data.iterrows():
            customer_id=row['customer_id']
            first_name=row['first_name']
            last_name=row['last_name']
            email=row['email']
            phone_no=row['phone_no']
            full_name=FullName(first_name=first_name,last_name=last_name)
            customer=Customer(customer_id=customer_id,
                              name=full_name,
                              email=email,phone_no=phone_no)
            customer_store.add_customer(customer)

          