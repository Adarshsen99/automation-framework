import json
import requests
from Dinero_api.testCases.login_logout.login_test import Test_Login

class Test_Edit:

    def test_delete_bank(self):
        self.auth_token = Test_Login.test_login(self)
        url = "http://api.dinero.local:8080/lookups/bank/?cmd=delete_bank"
        headers = {
            "Authorization": f"Token {self.auth_token}"
        }

        data ={
            "id":'1'
        }

        res = requests.post(url=url, headers=headers,json=data)
        print(json.dumps(res.json(), indent=4))
