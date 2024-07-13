import json
import os

import requests
from Dinero_api.testCases.login_logout.login_test import Test_Login

class Test_Edit:

    def test_get_id(self):
        self.auth_token = Test_Login.test_login(self)
        url = "http://api.dinero.local:8080/lookups/bank/?id=1"
        headers = {
            "Authorization": f"Token {self.auth_token}"
        }

        res = requests.get(url=url, headers=headers)
        print(json.dumps(res.json(), indent=4))


    # def test_edit(self):
    #     self.auth_token = Test_Login.test_login(self)
    #     url = "http://api.dinero.local:8080/lookups/bank/?cmd=edit_bank&id=1"
    #     headers = {
    #         "Authorization": f"Token {self.auth_token}"
    #     }
    #     data ={
    #         "bankname": "bank of edit",
    #         "bank_code": "boe",
    #         "bankname_in_local_lang": "boe",
    #         "bank_country": "2"
    #     }
    #     response = requests.post(url=url, headers=headers,json=data)
    #     print(json.dumps(response.json(),indent=4))




