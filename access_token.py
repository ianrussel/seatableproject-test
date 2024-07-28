import requests

api_token = "c7699b26b5a8e96874c8886ec545caeac99281f4"
def get_accestoken():
    url = "https://cloud.seatable.io/api/v2.1/dtable/app-access-token/"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {api_token}"
    }

    response = requests.get(url, headers=headers)

    return response.json()