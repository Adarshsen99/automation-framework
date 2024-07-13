import requests
import json
from Dinero_api.testCases.login_logout.login_test import Test_Login

class Test_edit:
    def test_edit_branch(self):
        self.auth_token = Test_Login().test_login()
        url = "http://api.dinero.local:8080/lookups/branch/?cmd=delete_branch"
        headers = {
            "Authorization": f"Token {self.auth_token}"
        }

        data ={
                "id":'144'
        }

        response = requests.post(url=url, headers=headers, json=data)
        print(json.dumps(response.json(), indent=4))


