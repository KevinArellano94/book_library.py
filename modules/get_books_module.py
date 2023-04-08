import os
from dotenv import load_dotenv
import requests
import json

def list_books(environment, query_name):
    load_dotenv(f"config/{ environment }.env")

    api_url = os.getenv('API_URL')
    api_id = os.getenv('API_ID')

    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_id
    }

    query = f"""
    query { query_name }
    {{
        { query_name }
        {{
            items
            {{
                id
                title
                author
            }}
        }}
    }}
    """

    response = requests.post(
        api_url,
        headers = headers,
        json = { "query": query }
    )
    
    return response.json()