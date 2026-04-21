import pandas as pd
import json
from json import JSONDecodeError
from src.models.customer import Customer
from src.models.full_name import FullName
from src.data_loader.customer_data_loader import CustomerDataLoader
from src.stores.customer_store_impl import CustomerStoreImpl

class CustomerJSONDataLoader(CustomerDataLoader):
    def load_data(self, file_path, customer_store: CustomerStoreImpl):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
        except JSONDecodeError:
            print(f"Warning: {file_path} is empty or invalid. No data loaded.")
            return

        # Convert JSON list/dict into DataFrame for iteration
        df = pd.DataFrame(data)
        print(f"Loaded DataFrame with {len(df)} rows:")
        print(df)

        for _, row in df.iterrows():
            customer_id = int(row['customer_id'])
            first_name = row['first_name']
            last_name = row['last_name']
            email = row['email']
            phone_no = row['phone_no']

            full_name = FullName(first_name=first_name, last_name=last_name)
            customer = Customer(
                customer_id=customer_id,
                name=full_name,
                email=email,
                phone_no=phone_no
            )
            customer_store.add_customer(customer)
            print(f"Added customer: {customer}")
