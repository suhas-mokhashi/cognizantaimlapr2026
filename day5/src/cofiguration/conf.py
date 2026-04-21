#create configuration file to load environment variables
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.app_env: str = os.getenv("APP_ENV", "development")
        self.resource_path: str = self.get_resource_path()

    def get_resource_path(self) -> str:
        if self.app_env == "production":
            return "src/resources/customer.json"
        elif self.app_env == "development":
            return "src/resources/customer.csv"
        else:
            return f"src/resources/customer.txt"

