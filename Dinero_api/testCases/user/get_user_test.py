import requests
import json
from Dinero_api.testCases.login_logout.login_test import Test_Login

class Test_edit:
    def test_edit_branch(self):
        self.auth_token = Test_Login().test_login()
        url = "http://api.dinero.local:8080/user/profile/"
        headers = {
            "Authorization": f"Token {self.auth_token}"
        }

        response = requests.get(url=url, headers=headers)
        print(json.dumps(response.json(), indent=4))