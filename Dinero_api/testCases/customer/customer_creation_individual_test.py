import requests
import json
from Dinero_api.testCases.login_logout.login_test import Test_Login

class Test_Post:
    url = "http://api.dinero.local:8080/customer/?cmd=add_customer"
    def test_post_individual(self):
        result = []
        self.auth_token = Test_Login().test_login()
        url = "http://api.dinero.local:8080/customer/?cmd=add_customer"
        headers = {
            "Authorization": f"Token {self.auth_token}"
        }
        file = open("/home/karunakar/PycharmProjects/Dinero_API/testData/customer/individual.json")
        payload = json.load(file)
        for data in payload:
            response = requests.post(url=url, headers=headers, json=data)
            result.append(response)
            print(json.dumps(response.json(), indent=4))

            assert response.status_code == 200
            assert response.headers['Content-Type'] == 'application/json'
            assert response.reason == "OK"




  #   def test_batch_requests(self):
  #
  #       data_list = {
  #           "type": "2",
  #           "title": "1",
  #           "firstname": "misriya",
  #           "middlename": "p",
  #           "lastname": "s",
  #           "nationality": "1",
  #           "arabicname": "جون",
  #           "fathername": "Michael",
  #           "dob": "1990-05-15",
  #           "place_of_birth": "kochi",
  #           "gender": "1",
  #           "marital_status": "1",
  #           "address1": "123 Main St",
  #           "address2": "123 sub St",
  #           "address3": "123 s St",
  #           "city": "New York",
  #           "country_adr": "1",
  #           "phone_no": "PONAAXC",
  #           "email": "59AQW0@example.com",
  #           "id_type": "1",
  #           "id_number": "ID85ADS",
  #           "id_expiry": "2025-05-15",
  #           "id_issue_country": "1",
  #           "visa_type": "1",
  #           "visa_no": "VIS1ASA665",
  #           "visa_expiry": "2025-05-15",
  #           "profession": "1",
  #           "employer": "ABC Corp",
  #           "employer_category": "1",
  #           "designation": "1",
  #           "source_of_income": "1",
  #           "salary_range": "1",
  #           "annual_income": "1",
  #           "purpose": "1",
  #           "loyalty_card_number": "LCQVNQW",
  #           "category": "1",
  #           "points": "100",
  #           "pep": "False",
  #           "documents": ["passfront.jpg"],
  #           "passports": [
  #               {
  #                   "nationality": "1",
  #                   "passport_number": "Ka254",
  #                   "issued_by": "1",
  #                   "passport_expiry": "2025-05-15"
  #               }
  #           ]
  # }
  #
  #       def test_make_request(data):
  #           count = 0
  #           self.auth_token = Test_Login().test_login()
  #           headers = {
  #                       "Authorization": f"Token {self.auth_token}"
  #                   }
  #
  #           res = requests.post(url=self.url, json=data, headers=headers)
  #
  #
  #           assert res.headers['Content-Type'] == 'application/json'
  #           assert res.reason == "OK"
  #
  #           start_time = time.time()
  #           res = requests.post(url=self.url, json=data_list)
  #           # end_time = time.time()
  #           # test_time = end_time - start_time
  #           #
  #           # print(f"Response Status Code: {res.status_code}")
  #           # print(f"Time Taken: {test_time / 1000} milliseconds")
  #
  #           if res.status_code == 200:
  #               count = count + 1
  #           print(count)
  #
  #       with ThreadPoolExecutor(max_workers=5000) as executor:
  #           executor.map(test_make_request, data_list)







