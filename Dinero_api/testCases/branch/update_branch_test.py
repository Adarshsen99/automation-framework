import requests
import json
from Dinero_api.testCases.login_logout.login_test import Test_Login

class Test_edit:
    def test_edit_branch(self):
        self.auth_token = Test_Login().test_login()
        url = "http://api.dinero.local:8080/lookups/branch/?cmd=edit_branch&id=243"
        headers = {
            "Authorization": f"Token {self.auth_token}"
        }

        data = {
          "bank_id" : "8",
          "branchname": "vtfvb ",
          "branchaddress": "trivandrum, near rr technopark",
          "branch_code": "tvmcrr",
          "branch_country" : "1",
          "branch_name_in_local_lang":"jhmaadshkhi"
        }

        response = requests.post(url=url, headers=headers, json=data)
        print(json.dumps(response.json(), indent=4))


