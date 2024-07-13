import requests
import json
from Dinero_api.testCases.login_logout.login_test import Test_Login

class Test_edit:
    def test_edit_branch(self):
        self.auth_token = Test_Login().test_login()
        url = "http://api.dinero.local:8080/user/profile/?cmd=add_user"
        headers = {
            "Authorization": f"Token {self.auth_token}"
        }


        data = {
            "first_name": "Parvathi",
            "last_name": "menon",
            "username": "5665655",
            "email": "pon@gmail.com",
            "company_branch": "1",
            "password": "paru123",
            "language_id": "1",
            "phone_no": "747410",
            "designation": "Makeup artist",
            "disable": "False",
            "preference": {
                "theme": "dark",
                "notifications": "true"
            }

        }
        response = requests.post(url=url, headers=headers, json=data)
        print(json.dumps(response.json(), indent=4))