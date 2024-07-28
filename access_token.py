import requests
import os
import sys
from dotenv import load_dotenv
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
script_dir = os.path.dirname(os.path.abspath(__file__))

dotenv_path = os.path.join(script_dir, '.env')
load_dotenv(dotenv_path=dotenv_path, override=True)

api_token = os.getenv('api_token')
def get_accestoken():
    url = "https://cloud.seatable.io/api/v2.1/dtable/app-access-token/"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {api_token}"
    }

    response = requests.get(url, headers=headers)

    return response.json()