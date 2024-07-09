import requests
import json
from Dinero_api.testCases.login_logout.login_local_test import Test_Login

class Test_Post:

    def test_post_individual(self):

        self.auth_token = Test_Login().test_login()
        url = "http://127.0.0.1:8000/api/currencytrade/?id=44"
        headers = {
            "Authorization": f"Token {self.auth_token}"
        }

        response = requests.get(url=url, headers=headers)
        print(json.dumps(response.json(), indent=4))

