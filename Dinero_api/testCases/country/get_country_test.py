
import requests
import jsonschema
import json
from testCases.login_logout.login_test import Test_Login

class Test_Get:
    def test_get(self):
        self.auth_token = Test_Login.test_login(self)
        url = "http://api.dinero.local:8080/lookups/country/"

        headers = {
            "Authorization": f"Token {self.auth_token}"
        }

        res = requests.get(url=url, headers=headers)
        # print(json.dumps(res.json(), indent=4))

        # Valiadtion
        assert res.status_code == 200, "Status code is not 200"
        assert res.headers['Content-Type'] == 'application/json'
        assert res.reason == "OK"
        # assert res.elapsed.microseconds/1000 < 50
        assert res.json()['type'] == 0
        assert res.json()['ok'] == True
        assert res.json()['response']['Country'][0]['id'] == 1
        assert res.json()['response']['Country'][1]['country_name'] == "Albania"
        assert res.json()['response']['Country'][2]['country_code'] == "DZA"
        assert res.json()['response']['Country'][3]['currency_name'] == "Euro"

        #Asserting value type

        assert isinstance(res.json()['response']['Country'][0]['id'],int)
        assert isinstance(res.json()['response']['Country'][1]['country_name'],str)
        assert isinstance(res.json()['response']['Country'][2]['country_code'],str)
        assert isinstance(res.json()['response']['Country'][3]['currency_name'],str)
        assert isinstance(res.json()['response'],object)
        assert isinstance(res.json()['response']['Country'], list)

        # Json Schema validation
        data_file = open("/home/karunakar/PycharmProjects/Dinero_API/testData/country/json_get.json")
        data = json.load(data_file)
        schema_file = open("/home/karunakar/PycharmProjects/Dinero_API/testData/country/schema_get.json")
        schema = json.load(schema_file)

        try:
            jsonschema.validate(instance=data, schema=schema)
            print("Validation successful")
        except jsonschema.ValidationError as e:
            print("Validation failed:", e)

     # search by region
    def test_get_region(self):
        self.auth_token = Test_Login.test_login(self)
        input_data = [0,'a', 'c', -1, "@", "tsr", " ", ".", ":", ";", "/","|","!?"]
        result = []
        count_pass = 0
        count_fail = 0
        for r in input_data:
            url = f"http://api.dinero.local:8080/lookups/country/?region={r}"

            headers = {
                "Authorization": f"Token {self.auth_token}"
            }

            res = requests.get(url=url, headers=headers)
            result.append(res)
            print(json.dumps(res.json(), indent=4))

            expect = f"Field 'id' expected a number but got '{r}'."
            act = res.json()['message']


            # Valiadtion
            assert res.status_code == 200, "Status code is not 200"
            assert res.headers['Content-Type'] == 'application/json'
            assert res.reason == "OK"

            # assertion
            if r != int:
                if act == expect:
                    print(f"Test data in region:",{r})
                    count_pass = count_pass + 1
                    print("Total Pass cases in region :",count_pass)
            else:
                count_fail = count_fail + 1
                print("Test Fail cases in region",count_fail)


     # search by country code
    def test_get_country_code(self):
        self.auth_token = Test_Login.test_login(self)
        input_country_code = ["Hell","AFG","ALB","DZA","AND","ARM",1,2,3,4,5,"@","@121","#","$","KULL"]
        result = []
        count_pass = 0
        count_fail = 0
        for code in input_country_code:
            url = f"http://api.dinero.local:8080/lookups/country/?country_code={code}"

            headers = {
                "Authorization": f"Token {self.auth_token}"
            }

            res = requests.get(url=url, headers=headers)
            result.append(res)
            # print("sent data",code,json.dumps(res.json(), indent=4))

            expect = "Country code must be at least 2 characters long and lessthan 3 characters long."
            act = res.json()['message']

            # Valiadtion
            assert res.status_code == 200, "Status code is not 200"
            assert res.headers['Content-Type'] == 'application/json'
            assert res.reason == "OK"

            # assertion

            if act == expect:
                print(f"Test data in country_code:", {code})
                count_pass = count_pass + 1
                print("Total Pass cases in country_code :",count_pass)
            else:
                count_fail = count_fail + 1
                print("Test Fail cases in country_code",count_fail)

     # search by currency
    def test_get_currency(self):
        self.auth_token = Test_Login.test_login(self)
        input_currency = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'c', -1, "@", "tsr", " ", ".", ":", ";", "/","|","!?"]
        result = []
        count_pass = 0
        count_fail = 0
        for currency in input_currency:
            url = f"http://api.dinero.local:8080/lookups/country/?currency={currency}"

            headers = {
                "Authorization": f"Token {self.auth_token}"
            }

            res = requests.get(url=url, headers=headers)
            result.append(res)
            # print("sent data", currency, json.dumps(res.json(), indent=4))

            expect = f"Field 'id' expected a number but got '{currency}'."
            act = res.json()['message']

            # Valiadtion
            assert res.status_code == 200, "Status code is not 200"
            assert res.headers['Content-Type'] == 'application/json'
            assert res.reason == "OK"

            # assertion
            if currency != int:
                if act == expect:
                    print(f"Test data in currency:",{currency})
                    count_pass = count_pass + 1
                    print("Total Pass cases in currency :",count_pass)
            else:
                count_fail = count_fail + 1
                print("Test Fail cases in currency",count_fail)
    #
    # #  search by countryName
    def test_get_country_name(self):
        self.auth_token = Test_Login.test_login(self)
        input_country_name= ["AFG","ALB","DZA","ANDO","ARM",0,1,2,3,4,5,"@","@1","#","$"]
        result = []
        count_pass = 0
        count_fail = 0
        for countryname in input_country_name:
            url = f"http://api.dinero.local:8080/lookups/country/?country_name={countryname}"

            headers = {
                "Authorization": f"Token {self.auth_token}"
            }

            res = requests.get(url=url, headers=headers)
            result.append(res)
            # print("sent data", countryname, json.dumps(res.json(), indent=4))
            #
            expect = "Country Name must be at least 3 characters long."
            act = res.json()['message']

            # Valiadtion
            assert res.status_code == 200, "Status code is not 200"
            assert res.headers['Content-Type'] == 'application/json'
            assert res.reason == "OK"

            # assertion

            if act == expect:
                print(f"Test pass data in country_name:", {countryname})
                count_pass = count_pass + 1
                print("Total Pass cases in country_name :", count_pass)
            else:
                # print(f"Test fail data in country_name:", {countryname})
                count_fail = count_fail + 1
                print("Test Fail cases in country_name:", count_fail)


