import json
import os

import requests
from testCases.login_logout.login_test import Test_Login

class Test_Edit:
    def test_edit(self):
        self.auth_token = Test_Login.test_login(self)
        url = "http://api.dinero.local:8080/lookups/bank/?cmd=edit_bank&id=2"
        headers = {
            "Authorization": f"Token {self.auth_token}"
        }
        file = open("/home/karunakar/PycharmProjects/Dinero_API/testData/bank/edit_bank_data.json")
        payload = json.load(file)

        for edit in payload:
            response = requests.post(url=url, headers=headers,json=edit)
            print(json.dumps(response.json(),indent=4))

            custom_location = '/home/karunakar/PycharmProjects/Dinero_API/testResultData/bank'

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Convert the JSON response to a Python dictionary
                new_data = response.json()
                # Check if the file exists
                filename = os.path.join(custom_location, 'response_data_edit_bank.json')
                if os.path.exists(filename):
                    # Read existing data from the file
                    with open(filename, 'r') as f:
                        existing_data = json.load(f)

                    # Append new data to the existing data
                    existing_data.append(new_data)
                else:
                    # If the file doesn't exist, create a new list with new_data
                    existing_data = [new_data]

                # Save the combined JSON data to the file
                with open(filename, 'w') as f:
                    json.dump(existing_data, f, indent=4)

                print("JSON edit response appended to the file successfully.")
            else:
                print("Error:", response.status_code)



