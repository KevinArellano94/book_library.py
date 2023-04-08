import requests
import json

def add_book(api_url, api_id, author, title, query_name):
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_id
    }

    mutation = f"""
    mutation { query_name }($input: CreateMyModelTypeInput!) 
    {{
        { query_name }(input: $input)
        {{
            id
            title
            author
        }}
    }}
    """

    variables = {
        "input":
        {
            "title": title,
            "author": author
        }
    }

    data = {
        "query": mutation,
        "variables": variables
    }

    response = requests.post(
        api_url,
        headers = headers,
        data=json.dumps(data)
    )
    
    return json.dumps(response.json(), indent = 4)