import requests
import json
from Dinero_api.testCases.login_logout.login_local_test import Test_Login

class Test_Post:
    url = "http://api.dinero.local:8080/customer/?cmd=add_customer"

    def test_post_individual(self):
        self.auth_token = Test_Login().test_login()
        url = "http://127.0.0.1:8000/api/customer/?cmd=edit_customer&id=1"
        headers = {
            "Authorization": f"Token {self.auth_token}"
        }

        passport = [
            {
                "id": '5',
                "nationality": '1',
                "passport_number": "HHJKLdrtT1J23987",
                "issued_by": '1',
                "passport_expiry_date": "2030-12-15",
                "passport_issue_date": "2024-03-10",
                "passport_type": '1'
            }
        ]

        relationship = [
            {"related_to": '1', "relation": '1'}
        ]

        delegates = [
            {
                "delegate_id": '6',
                "validity": '1',
                "validity_start_date": "2024-05-15",
                "validity_end_date": "2025-05-15"
            }
        ]

        documents = [
            {
                "id": 5,
                "side": "home"
            }
        ]

        data = {
            "type": 1,
            "title": 1,
            "first_name": "Devika",
            "middle_name": "",
            "last_name": "Pillai",
            "arabic_name": "عبد الرحمن",
            "short_name": "devi",
            "maiden_name": "manukuttan",
            "dob": "1998-03-23",
            "country_of_birth": 1,
            "nationality": 1,
            "citizenship_by": 1,
            "country_of_residence": 1,
            "residential_status": 1,
            "gender": 1,
            "marital_status": 1,
            "profession": 1,
            "address1": "Amaravathy Fortkochi",
            "address2": "Ernakulam",
            "address3": "thoppumpady",
            "state_name": "kochi",
            "city": "pattaalam",
            "email": "Devika@gmail.com",
            "country_adr": 1,
            "phone_no": "048456987",
            "is_non_resident": "true",
            "nonRes_city": "",
            "nonRes_country": "",
            "visa_type": 1,
            "visa_no": "155564",
            "visa_issue_date": "2023-03-15",
            "visa_expiry_date": "2030-03-23",
            "remarks_contact": "",
            "id_type": 1,
            "id_number": "0005022223",
            "id_place_of_issue": "Qatar",
            "id_issue_date": "2018-05-20",
            "id_expiry": "2030-05-20",
            "fax": "",
            "purpose": 1,
            "organization_category": 1,
            "designation": 1,
            "employer": "MT Company",
            "employer_category": 1,
            "employer_description": 1,
            "source_of_income": 1,
            "salary_range": 1,
            "annual_income": 1,
            "other_source_of_income": "",
            "monthly_income_range": "",
            "demographics": 1,
            "industry_type": 1,
            "employment": 1,
            "employee_type": 1,
            "professional_email": "Devika@gmail.com",
            "role": 1,
            "remarks_role": "good",
            "special_needs": "True",
            "detailsof_sp_needs": 1,
            "remarks_of_sp_needs": "",
            "pep": "False",
            "remarks_pep": "",
            "institution_name": "Hydai",
            "institution_type": 1,
            "membership_type": 1,
            "loyalty_card_number": "150074",
            "loyalty_category": 1,
            "points": 201,
            "cust_nearest_airport": "Kochi International",
            "cust_segment": 1,
            "intrested_in_remittance": "False",
            "exptd_annual_activity_remtc_vol": "",
            "exptd_annual_activity_remtc_nos": "",
            "intrested_in_fastcash": "False",
            "exptd_annual_activity_fc_vol": "",
            "exptd_annual_activity_fc_nos": "",
            "cb_purpose": 1,
            "consent_mrkt": "False",
            "by_whatsapp": "False",
            "by_phone": "False",
            "by_fax": "False",
            "by_postal_mail": "False",
            "by_email": "False",
            "facebook": "",
            "twitter": "",
            "instagram": "",
            "linkedin": "",
            "website": "",
            "whatsapp": "",
            "access": "False",
            "consent1": "False",
            "consent2": "False",
            "consent3": "False",
            "reg_remarks": "False",
            "investigation_details": "",
            "appl_priority": 1,
            "passports": json.dumps(passport),
            "relationships": json.dumps(relationship),
            "delegates": json.dumps(delegates),
            "documents": json.dumps(documents)
        }

        # Reading file data
        with open("/home/karunakar/DineroQa/Dinero_api/testData/images/documents.png", "rb") as file:
            files = {
                "delegates_documents": ("documents.png", file, "image/png")
            }

            response = requests.post(url=url, headers=headers, data=data, files=files)
            print(json.dumps(response.json(), indent=4))
