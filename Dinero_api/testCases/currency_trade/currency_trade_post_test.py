import requests
import json
from Dinero_api.testCases.login_logout.login_local_test import Test_Login

class Test_Post:
    def test_post_individual(self):

        self.auth_token = Test_Login().test_login()
        url = "http://127.0.0.1:8000/api/currencytrade/?cmd=record_currency_trade"
        headers = {
            "Authorization": f"Token {self.auth_token}"
        }

        data = {
            "date":"2024-07-13",
            "trasaction_type": "1",
            "customer_id": "6",
            "transaction_mode": "1",
            # "delegate_id": "2",
            "transaction_purpose": "1",
            "source_of_income": "1",
            "pos_bank": "1",
            "rate": "10",
            "vat": "1",
            "lc_total_due": "100",
            "trasaction_details": "10",
            "tax": "10.99",
            "rounded_amount": "10",
            "tansfer_type": "2",
            "cheque_bank": "1",
            "currency": "1",
            "fc_amount": "1231",
            "lc_received": "1",
            "balance_paid": "2",
            "payment_amount_cash": "50",
            "cash": "50",
            "pos_amount": "20",
            "cheque_amount": "30",
            "online_amount": "0",
            "digital_pay": "0" ,
            "record_no":"71717",
            "transaction_reference":"61661662",
            "cheque_date":"2024-07-15",
        }
        response = requests.post(url=url, headers=headers, data=data)
        print(json.dumps(response.json(), indent=4))
