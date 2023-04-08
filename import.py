import os
from dotenv import load_dotenv
import requests
import json

environment = "development"

load_dotenv(f"config/{ environment }.env")

api_url = os.getenv('API_URL')
api_id = os.getenv('API_ID')

author = "Frédéric Bastiat"
title = "The Law"

headers = {
    "Content-Type": "application/json",
    "x-api-key": api_id
}

mutation = """
mutation createMyModelType($createmymodeltypeinput: CreateMyModelTypeInput!) 
{
    createMyModelType(input: $createmymodeltypeinput)
    {
        id
        title
        author
    }
}
"""

variables = {
    "createmymodeltypeinput":
    {
        "title": title,
        "author": author
    }
}

data = {
    "query": mutation,
    "variables": variables
}

response = requests.post(api_url, headers=headers, data=json.dumps(data))
print(response.json())
