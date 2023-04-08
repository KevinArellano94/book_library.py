from modules.get_books_module import list_books

environment = "development"

result = list_books(environment, query_name = "listMyModelTypes")
print(result)