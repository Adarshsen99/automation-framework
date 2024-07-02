import json
import requests

from Utilities.custom_Logger import LogGen
LogGen.loggen().info("**** Request sent ****")

class Test_Login:

    def test_login(self):
        url = "http://api.dinero.local:8080/user/login/"

        payload = {
            "username": "root",
            "password": "admin"
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url, json=payload, headers=headers)

        auth_token = response.json()["response"]["auth_token"]
        return auth_token

