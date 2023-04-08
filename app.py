import os
from dotenv import load_dotenv
from modules.get_books_module import list_books
from modules.add_book_module import add_book

environment = "development"

load_dotenv(f"config/{ environment }.env")
api_url = os.getenv('API_URL')
api_id = os.getenv('API_ID')

result = list_books(api_url, api_id, query_name = "listMyModelTypes")
print(result)

author = "Anthony Burgess"
title = "A Clockwork Orange"

result = add_book(api_url, api_id, author, title, query_name = "createMyModelType")
print(result)