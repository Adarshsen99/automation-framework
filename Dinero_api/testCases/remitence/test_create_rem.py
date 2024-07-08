import requests
import json
import random
import string
from Dinero_api.testCases.login_logout.login_test import Test_Login

class Test_R:
    def generate_random_string(self, length=5):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(length))

    def generate_random_number(self, max_digits=2):

        return str(random.randint(1, 10**max_digits - 1))

    def test_post_corporate(self):
        self.auth_token = Test_Login().test_login()
        url = "http://api.dinero.local:8080/remittance/?cmd=record_remittance"
        headers = {
            "Authorization": "Token 5479686c0ade6a0d8ac8ab2c1a8c3142ce6aff21cb7dc12a5020e904aeae3212"
        }
        cust = ["109","110","111"]

        for _ in range(1):
            lc = self.generate_random_number(10)
            for i in cust:
                data = {
                    "trans_type": "1",
                    "customer": i,
                    "trans_mode": "1",
                    "beneficiary": "9",
                    "beneficiarybank": "8",
                    "remittance_purpose": "1",
                    "source_of_income": "1",
                    "service_provider": "1",
                    "currency": "1",
                    "fc_amount": lc,
                    "rate": lc,
                    "reverse_rate": lc,
                    "lc_amount": lc,
                    "service_charge": lc,
                    "tax": lc,
                    "rounded_amount": lc,
                    "lc_total_due": lc,
                    "vat": lc,
                    "by_cash": "True",
                    "payment_amount_cash": lc,
                    "lc_received": lc,
                    "transaction_pin": self.generate_random_string(5)

                }

            response = requests.post(url=url, headers=headers, json=data)
            print(f"Response {_+1}:")
            print(json.dumps(response.json(), indent=4))

