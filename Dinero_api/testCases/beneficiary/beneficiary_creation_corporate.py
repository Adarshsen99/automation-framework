import requests
import json
from testCases.login_logout.login_test import Test_Login


class Test_Creation_Individual():
    def test_creation_individual(self):
        result = []
        self.auth_token = Test_Login().test_login()
        url = "http://api.dinero.local:8080/beneficiary/?cmd=add_beneficiary"
        headers = {
            "Authorization": f"Token {self.auth_token}"
        }
        file = open("/home/karunakar/PycharmProjects/Dinero_API/testData/Benificiary/corporate_creation.json")
        payload = json.load(file)
        for data in payload:
            response = requests.post(url=url, headers=headers, json=data)
            result.append(response)
            print(json.dumps(response.json(), indent=4))

            assert response.status_code == 200
            assert response.headers['Content-Type'] == 'application/json'
            assert response.reason == "OK"
