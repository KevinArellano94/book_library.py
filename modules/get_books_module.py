import requests
import json

def list_books(api_url, api_id, query_name):
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
    
    return json.dumps(response.json(), indent = 4)