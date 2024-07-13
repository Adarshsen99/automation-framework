import requests
import json
from Dinero_api.testCases.login_logout.login_test import Test_Login
from Dinero_api.Utilities.random_generator import Random

class Test_Add:
    def test_get_by_passing_bank_id(self):
        self.auth_token = Test_Login().test_login()

        # print(self.auth_token)
        url = "http://api.dinero.local:8080/lookups/branch/?bank_id=35"

        headers = {
            "Authorization": f"Token {self.auth_token}"
        }
        response = requests.get(url=url, headers=headers)
        print(json.dumps(response.json(), indent=4))

    # def test_get_by_passing_bank_id_branchname(self):
    #     self.auth_token = Test_Login().test_login()
    #
    #     # print(self.auth_token)
    #     url = "http://api.dinero.local:8080/lookups/branch/?bank_id=8&branch_name=CjqLI"
    #
    #     headers = {
    #         "Authorization": f"Token {self.auth_token}"
    #     }
    #     response = requests.get(url=url, headers=headers)
    #     print(json.dumps(response.json(), indent=4))