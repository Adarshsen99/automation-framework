import json
import requests

from Dinero_api.Utilities.custom_Logger import LogGen
LogGen.loggen().info("**** Request sent ****")

class Test_Login:

    def test_login(self):
        url = "http://127.0.0.1:8000/api/user/login/"

        payload = {
            "username": "admin",
            "password": "admin"
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url, json=payload, headers=headers)

        auth_token = response.json()["response"]["auth_token"]
        return auth_token

