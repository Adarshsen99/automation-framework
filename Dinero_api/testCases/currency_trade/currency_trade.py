import requests
import json
from Dinero_api.testCases.login_logout.login_local_test import Test_Login

class Test_Post:
    url = "http://127.0.0.1:8000/api/currencytrade/?cmd=record_currency_trade"
    def test_post_individual(self):

        self.auth_token = Test_Login().test_login()
        url = "http://127.0.0.1:8000/api/currencytrade/?cmd=record_currency_trade"
        headers = {
            "Authorization": f"Token {self.auth_token}"
        }

        data = {
            "date":"2024-07-12",
            "trasaction_type": "1",
            "customer_id": "1",
            "transaction_mode": "1",
            "delegate_id": "1",
            "transaction_purpose": "1",
            "source_of_income": "1",
            "pos_bank": "1",
            "rate": "10",
            "vat": "1",
            "lc_total_due": "100",  # Ensure this matches the sum of all payments
            "trasaction_details": "10",
            "tax": "10",
            "rounded_amount": "10",
            "tansfer_type": "2",
            "cheque_bank": "1",
            "currency": "1",
            "fc_amount": "1231",
            "Lc_received": "10",
            "balance_paid": "2",
            "payment_amount_cash": "50",  # Ensure these values add up to lc_total_due
            "cash": "50",  # Ensure these values add up to lc_total_due
            "pos_amount": "20",  # Ensure these values add up to lc_total_due
            "cheque_amount": "30",  # Ensure these values add up to lc_total_due
            "online_amount": "0",  # Ensure these values add up to lc_total_due
            "digital_pay": "0" ,
            "record_no":"7171717162",
            "transaction_reference":"6166161662",
            "cheque_date":"2024-07-19",

        }

        response = requests.post(url=url, headers=headers, data=data)
        print(json.dumps(response.json(), indent=4))
