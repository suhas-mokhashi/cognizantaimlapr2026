# creating entry point for application
import faker
from store.customerstore import CustomerStore
from view.customerview import CustomerView

"""creating application entry point to display name
call the customer store and customer view to display the customers"""


def check():
    """this function creates an instance of faker and prints a name"""
    customer_store = CustomerStore(num_customers=100)
    customer_view = CustomerView(customer_store)
    customer_view.display_customers()



if __name__ == "__main__":
    check()
