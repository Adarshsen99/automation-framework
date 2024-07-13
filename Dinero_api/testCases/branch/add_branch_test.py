import requests
import json
from Dinero_api.testCases.login_logout.login_test import Test_Login
from Dinero_api.Utilities.random_generator import Random

class Test_Add:
    def test_add(self):
        self.auth_token = Test_Login().test_login()

        # print(self.auth_token)
        url = "http://api.dinero.local:8080/lookups/branch/?cmd=add_branch"

        headers = {
            "Authorization": f"Token {self.auth_token}"
        }

        bank_id = [20,33,34,30,35,22,17,8,18,23,21]
        country = [1,2,3,4,5,6,7]
        
        for _ in range(1):
            for i,j in zip(bank_id,country):
                self.string = Random().generate_random_string()
                self.number = Random().generate_random_number()
                self.alphanumeric = Random().generate_random_alphanumeric()
                self.special_char = Random().generate_random_special_characters()
                self.special_char_and_letter = Random().generate_random_special_and_string_characters()
                self.special_char_and_number = Random().generate_random_special_and_string_number()

                data = {
                    "bank_id": str(i),
                    "branchname": self.string,
                    "branchaddress": self.string,
                    "branch_code": self.alphanumeric,
                    "branch_country": str(j),
                    "branch_name_in_local_lang": self.string
                }

                response = requests.post(url=url, headers=headers, json=data)
                print(json.dumps(response.json(), indent=4))




