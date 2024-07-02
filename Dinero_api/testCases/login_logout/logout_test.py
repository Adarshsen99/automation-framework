import requests

from testCases.login_logout.login_test import Test_Login


class Test_Logout:

    def test_logout(self):
        self.auth_token = Test_Login.test_login(self)
        url_out = "http://api.dinero.local:8080/user/logout/"

        headers = {
            "Authorization": f"Token {self.auth_token}"
        }
        payload = {
            "logout": "true"
        }

        response = requests.post(url_out, headers=headers, json=payload)

        print("Logout responce:", response.json())

        # Validation
        if response.json()['ok'] == True:
            assert True
        else:
            assert False

        assert response.status_code == 200, "Status code is not 200"

        if isinstance(response.json()['message'], str) and isinstance(response.json()['type'], int) and isinstance(
                response.json()['error'], str):
            assert True
        else:
            assert False

        assert response.json()['type'] == 0
        assert response.json()['message'] == "Logged out"
        assert response.json()['response'] is None
        assert response.headers['Content-Type'] == 'application/json'


