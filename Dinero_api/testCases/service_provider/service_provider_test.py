import requests
import json


from Dinero_api.testCases.login_logout.login_test import Test_Login


class Test_Servide_Provider():
    def test_post_service_provider(self):
        self.auth_token = Test_Login.test_login(self)
        url = "http://127.0.0.1:8000/api/serviceprovider/?cmd=add_serviceprovider"

        headers = {
             "Authorization": f"Token {self.auth_token}",
            "languagecode": "fr"
        }

        with open("/home/karunakar/DineroQa/Dinero_api/testData/images/Screenshot from 2024-07-02 18-17-37.png", "rb") as file:
            file_data = file.read()

        fund_currencies = [
            {"currency": "2", "rate": "1.2345", "settlement_rate": "1.22", "pay_in_settlement_rate": "1.23", "balance_alert_trigger": "5000"},
            {"currency": "1", "rate": "1.2345", "settlement_rate": "1.22", "pay_in_settlement_rate": "1.23", "balance_alert_trigger": "5000"}
        ]

        payout_profiles = [
            {
                "country": "1",
                "country_code": "US",
                "currency": "1",
                "currency_code": "840",
                "transfer_type": "1",
                "date_format": "1",
                "cost_rate_source": "1",
                "fund_currency": "1",
                "api_avilable": "true",
                "deal_required": "true",
                "deal_balance_alert": "10000",
                "transaction_approval_required": "false",
                "batch_processing_required": "true",
                "customer_sms_required": "false",
                "insufficient_balance_mode": "1",
                "over_draft_limit": "5000",
                "over_draft_limit_alert": "Email",
                "individual_to_individual": "true",
                "individual_to_individual_transaction_limit": "true",
                "individual_to_individual_transaction_limit_currency": "1",
                "individual_to_corporate": "false",
                "individual_to_corporate_transaction_limit": "true",
                "individual_to_corporate_transaction_limit_currency": "1",
                "corporate_to_individual": "true",
                "corporate_to_individual_transaction_limit": "false",
                "corporate_to_individual_transaction_limit_currency": "1",
                "corporate_to_corporate": "false",
                "corporate_to_corporate_transaction_limit": "false",
                "corporate_to_corporate_transaction_limit_currency": "1",
                "sc_from_api": "true",
                "amount_wise_sc": "true",
                "sc_currency": "1",
                "sc_share_mode": "1",
                "sc_slab_currency": "1",
                "sc": "1.5",
                "share_factor": "0.02",
                "amount_wise_sc_slab": [
                    {
                        "branch": "1",
                        "from_amount": "10000",
                        "to_amount": "20000",
                        "sc": "5.78"
                    }
                ],
                "incentive": "true",
                "incentive_mode": "1",
                "incentive_settlement_cycle": "1",
                "amount_wise_incentive": "false",
                "incentive_slab_currency": "1",
                "incentive_currency": "1",
                "amount_wise_incentive_slab": [],
                "third_party_bank_deposit_charges": "false",
                "other_bank_deposit_charges": "true",
                "other_bank_deposit_currency": "1",
                "other_bank_deposit_slab_currency": "1",
                "deposit_charges": "10.0",
                "amount_wise_deposit_charge_slab": [],
                "active_status": "true"
            }
        ]

        data = {
            "category": "1",
            "bank": "1",
            "name": "Example Bank Ltd.",
            "arabic_name": "مصرف المثال",
            "address1": "123 Main Street",
            "address2": "Apt 101",
            "address3": "",
            "postal_code": "12345",
            "city": "Exampleville",
            "country": "1",
            "countryof_incorporation": "1",
            "phone_number": "++857w8878787",
            "email": "info@ex3745658bank.com",
            "agrmnt_start_date": "2023-01-01",
            "agrmnt_end_date": "2028-12-31",
            "reg_no": "AtBC15667582w47l2e7s23",
            "reg_expiry_date": "2025-06-30",
            "trade_license_no": "DEF7786345we27l57ts4656",
            "trade_license_expiry_date": "2024-12-31",
            "license_no": "GHI577w6s745832zl68te9",
            "licensing_auth": "Example Licensing Authority",
            "auth_person_name": "John Doe",
            "gender": "1",
            "dob": "1985-05-15",
            "country_of_birth": "1",
            "nationality": "1",
            "fund_currencies": json.dumps(fund_currencies),
            "payout_profiles": json.dumps(payout_profiles)
        }

        files = {
            "uploaded_documents": ("image.png", file_data, "image/png")
        }

        response = requests.post(url=url, headers=headers, data=data, files=files)
        print(json.dumps(response.json(), indent=4))

  

