import os
from dotenv import load_dotenv
from modules.get_books_module import list_books

environment = "development"

load_dotenv(f"config/{ environment }.env")
api_url = os.getenv('API_URL')
api_id = os.getenv('API_ID')

result = list_books(api_url, api_id, query_name = "listMyModelTypes")

print(result)