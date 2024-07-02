import json

import requests
from testCases.login_logout.login_test import Test_Login

class Test_Get:
    def test_get(self):
        self.auth_token = Test_Login.test_login(self)
        url = "http://api.dinero.local:8080/lookups/bank/"
        headers = {
             "Authorization": f"Token {self.auth_token}"
         }

        res = requests.get(url=url,headers=headers)

        print(json.dumps(res.json(),indent=4))

        # Valiadtion
        assert res.status_code == 200, "Status code is not 200"
        assert res.headers['Content-Type'] == 'application/json'
        assert res.reason == "OK"
        # assert res.elapsed.microseconds/1000 < 50
        assert res.json()['type'] == 0
        assert res.json()['ok'] == True
        assert res.json()['response']['banks'][0]['id'] == 5
        assert res.json()['response']['banks'][1]['bankname'] == "1"
        assert res.json()['response']['banks'][0]['country']['id'] == 1
        assert res.json()['response']['banks'][0]['country']['country_code'] == "AFG"
        assert res.json()['response']['banks'][0]['country']['country_name'] == "Afghanistan"
        assert res.json()['response']['banks'][0]['country']['currency']['id'] == 1
        assert res.json()['response']['banks'][0]['country']['currency']['currency_name'] == "Afghan Afghani"
        assert res.json()['response']['banks'][0]['country']['currency']['currency_code'] == "AFN"
        assert res.json()['response']['banks'][0]['country']['region']['id'] == 1
        assert res.json()['response']['banks'][0]['country']['region']['region'] == 'Asia'
        assert res.json()['response']['banks'][0]['country']['sub_region']['id'] == 1
        assert res.json()['response']['banks'][0]['country']['sub_region']['subregion'] == "Southern Asia"

        # Asserting value type

        assert isinstance(res.json()['response']['banks'][0]['id'], int)
        assert isinstance(res.json()['response']['banks'][1]['bankname'], str)
        assert isinstance(res.json()['response']['banks'][0]['country'], object)
        assert isinstance(res.json()['response']['banks'][0]['country']['id'], int)
        assert isinstance(res.json()['response']['banks'][0]['country']['country_code'], str)
        assert isinstance(res.json()['response']['banks'][0]['country']['country_name'], str)
        assert isinstance(res.json()['response']['banks'][0]['country']['currency'], object)
        assert isinstance(res.json()['response']['banks'][0]['country']['currency']['id'], int)
        assert isinstance(res.json()['response']['banks'][0]['country']['currency']['currency_name'], str)
        assert isinstance(res.json()['response']['banks'][0]['country']['currency']['currency_code'], str)
        assert isinstance(res.json()['response']['banks'][0]['country']['region'], object)
        assert isinstance(res.json()['response']['banks'][0]['country']['region']['id'], int)
        assert isinstance(res.json()['response']['banks'][0]['country']['region']['region'], str)
        assert isinstance(res.json()['response']['banks'][0]['country']['sub_region'], object)
        assert isinstance(res.json()['response']['banks'][0]['country']['sub_region']['id'], int)
        assert isinstance(res.json()['response']['banks'][0]['country']['sub_region']['subregion'], str)

    #search by id
    def test_get_id(self):
        self.auth_token = Test_Login.test_login(self)
        id_input_data = [1,2,3,4,"@","a","A","@1","@b","%$","finnest",5,123]
        print(id_input_data)
        result = []
        count = 0
        count_int = 0
        for id in id_input_data:
            url = f"http://api.dinero.local:8080/lookups/bank/?id={id}"
            headers = {
                "Authorization": f"Token {self.auth_token}"
            }

            res = requests.get(url=url, headers=headers)
            result.append(res)
            print(f"data sent:{id}",json.dumps(res.json(),indent=4))

            expect = f"Field 'id' expected a number but got '{id}'."
            act = res.json()['message']

            assert res.status_code == 200, "Status code is not 200"
            assert res.headers['Content-Type'] == 'application/json'
            assert res.reason == "OK"

            # assertion
            if id != int :
                if expect == act:
                    count = count+1
                    print("Total string data:", count)
                    assert True
            else:
                assert False

            if isinstance(id, int) and len(str(id)) >= 3:
                count_int = count_int + 1
                print(f"int more than 3 :", count_int)

            else:
                print("")

    #search by name
    def test_get_name(self):
        self.auth_token = Test_Login.test_login(self)
        name_input_data = [1,2,3,4,"@","a","A","@1","@b","%$","finnest",5,"hfufn",":::"]
        count = 0
        result_name = []
        for name in name_input_data:
            url = f"http://api.dinero.local:8080/lookups/bank/?name={name}"
            headers = {
                "Authorization": f"Token {self.auth_token}"
            }

            res = requests.get(url=url, headers=headers)
            result_name.append(res)
            print(f"data sent:{name}",json.dumps(res.json(),indent=4))


            assert res.status_code == 200, "Status code is not 200"
            assert res.headers['Content-Type'] == 'application/json'
            assert res.reason == "OK"

            # assertion

            if isinstance(name, str) and len(name) >= 2 or name == '@':
                if len(res.json()['response']['banks']) == 0:
                    count = count + 1
                    assert True

                else:
                    assert False
            print(f"strs:{name}", count)
