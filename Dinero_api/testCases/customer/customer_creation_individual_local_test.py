import requests
import json
from Dinero_api.testCases.login_logout.login_local_test import Test_Login

class Test_Post:
    url = "http://api.dinero.local:8080/customer/?cmd=add_customer"
    def test_post_individual(self):
        result = []
        self.auth_token = Test_Login().test_login()
        url = "http://127.0.0.1:8000/api/customer/?cmd=add_customer"
        headers = {
            "Authorization": f"Token {self.auth_token}"
        }

        passports = [
            {
                "nationality": "1",
                "passport_number": "HHJKLdT123987",
                "issued_by": "1",
                "passport_expiry_date": "2030-05-15",
                "passport_issue_date": "2024-12-10",
                "passport_type": "1"

            }
        ]

        data = {
                "type": "1",
                "title": "1",
                "first_name": "Misriya",
                "middle_name": "name",
                "last_name": "TS",
                "arabic_name": "عبد الرحمن",
                "short_name": "michu",
                "maiden_name": "jo",
                "dob": "1998-03-11",
                "country_of_birth": "1",
                "nationality": "1",
                "citizenship_by": "1",
                "country_of_residence": "1",
                "residential_status": "1",
                "gender": "2",
                "marital_status": "1",
                "profession": "1",
                "address1": "Rose Main St",
                "address2": "Apt 45",
                "address3": "fff",
                "state_name": "kochi",
                "city": "pattaalam",
                "email": "misriydfats@gmail.com",
                "country_adr": "1",
                "phone_no": "7896df54112",
                "is_non_resident": True,
                "nonRes_address1": None,
                "nonRes_address2": None,
                "nonRes_address3": None,
                "nonRes_state_name": None,
                "nonRes_city": None,
                "nonRes_country": None,
                "visa_type": "1",
                "visa_no": "00df2365",
                "visa_issue_date": "2023-03-15",
                "visa_expiry_date": "2030-03-15",
                "remarks_contact": None,
                "id_type": "1",
                "id_number": "77df777855",
                "id_place_of_issue": "dubai",
                "id_issue_date": "2010-05-20",
                "id_expiry": "2030-05-20",
                "fax": None,
                "purpose": "1",
                "organization_category": "1",
                "designation": "1",
                "employer": "michukutty Company",
                "employer_category": "1",
                "employer_description": "1",
                "source_of_income": "1",
                "salary_range": "1",
                "annual_income": "1",
                "other_source_of_income": None,
                "monthly_income_range": None,
                "demographics": "1",
                "industry_type": "1",
                "employment": "1",
                "employee_type": "1",
                "professional_email": "misriydfaofficial@gmail.com",
                "role": "1",
                "remarks_role": None,
                "special_needs": "True",
                "detailsof_sp_needs": "1",
                "remarks_of_sp_needs": None,
                "pep": "False",
                "remarks_pep": None,
                "institution_name": "ak",
                "institution_type": "1",
                "membership_type": "1",
                "loyalty_card_number": "11122df233",
                "loyalty_category": "1",
                "points": "201",
                "cust_nearest_airport": "kochi",
                "cust_segment": "1",
                "intrested_in_remittance": "False",
                "exptd_annual_activity_remtc_vol": None,
                "exptd_annual_activity_remtc_nos": None,
                "intrested_in_fastcash": "False",
                "exptd_annual_activity_fc_vol": None,
                "exptd_annual_activity_fc_nos": None,
                "cb_purpose": "1",
                "consent_mrkt": "False",
                "by_whatsapp": "False",
                "by_phone": "False",
                "by_fax": "False",
                "by_postal_mail": "False",
                "by_email": "False",
                "facebook": None,
                "twitter": None,
                "instagram": None,
                "linkedin": None,
                "website": None,
                "whatsapp": None,
                "access": "False",
                "consent1": "False",
                "consent2": "False",
                "consent3": "False",
                "reg_remarks": "False",
                "investigation_details": None,
                "appl_priority": None,
                "passports": json.dumps(passports),
            }

        with open("/home/karunakar/DineroQa/Dinero_api/testData/images/Screenshot from 2024-07-02 18-17-37.png", "rb") as file:
            file_data = file.read()
        files = {
                "upload_documents": ("image.png", file_data, "image/png")
        }

        response = requests.post(url=url, headers=headers, data=data, files=files)
        print(json.dumps(response.json(), indent=4))



