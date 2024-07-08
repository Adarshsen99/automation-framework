import requests
import json
from testCases.login_logout.login_test import Test_Login


class Test_Customer_Delete():
    def test_delete(self):

        self.auth_token = Test_Login().test_login()
        url = "http://api.dinero.local:8080/customer/?cmd=delete_customer"
        headers = {
            "Authorization": f"Token {self.auth_token}"
        }
        data = { "id":"118"}

        response = requests.post(url=url, headers=headers, json=data)
        print(json.dumps(response.json(), indent=4))