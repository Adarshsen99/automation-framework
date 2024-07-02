import requests
from concurrent.futures import ThreadPoolExecutor
import json
import time

class Test_messages:
    url = "http://mld.dinero.local:8081/?cmd=message"

    def test_messages(self):
        screen_id = "user"
        source_text = "partner"

        data_list = [
            {
                "screen_id": "applications",
                "source_text": "firefox",
                "language_code": "fr"
            },
            {
                "screen_id": "",
                "source_text": "",
                "language_code": "fr"
            },
            {

            },
            {
                "screen_id": 1,
                "source_text": 3,
                "language_code": 2
            },
            {
                "screen_id": screen_id,
                "source_text": source_text,
                "language_code": "fr"
            },
            {
                "screeners_id": screen_id,
                "sources_text": source_text,
                "luggage_code": "fr"
            },
            {
                "creen_id": screen_id,
                "source_text": source_text,
                "language_code": "fr"
            },
            {
                "screen_id": screen_id,
                "ource_text": source_text,
                "language_code": "fr"
            },
            {
                "screen_id": screen_id,
                "source_text": source_text,
                "anguage_code": "fr"
            },
            {
                "screen_i": screen_id,
                "source_text": source_text,
                "language_code": "fr"
            },
            {
                "screen_id": screen_id,
                "source_tex": source_text,
                "language_code": "fr"
            },
            {
                "screen_id": screen_id,
                "source_text": source_text,
                "language_cod": "fr"
            },
            {
                "ascreen_id": screen_id,
                "source_text": source_text,
                "language_code": "fr"
            },
            {
                "screen_id": screen_id,
                "bsource_text": source_text,
                "language_code": "fr"
            },
            {
                "screen_id": screen_id,
                "source_text": source_text,
                "clanguage_code": "fr"
            },
            {
                "screen_ida": screen_id,
                "source_text": source_text,
                "language_code": "fr"
            },
            {
                "screen_id": screen_id,
                "source_textb": source_text,
                "language_code": "fr"
            },
            {
                "screen_id": screen_id,
                "source_text": source_text,
                "language_codec": "fr"
            },
            {
                "screen_id": screen_id,

            },
            {

                "source_text": source_text,

            },
            {

                "language_code": "fr"
            },
            {
                "screen_id": screen_id,
                "source_text": source_text,

            },
            {

                "source_text": source_text,
                "language_code": "fr"
            },
            {
                "screen_id": screen_id,

                "language_code": "fr"
            },

        ]

        def make_request(data):
            res_not_200 = []
            res_not_type = []
            res_not_ok = []
            res_message = []
            res = requests.post(url=self.url, json=data)
            print(json.dumps(res.json(), indent=4))
            print(res.status_code)

            if res.status_code == 200:
                assert True
            else:
                res_not_200.append(json.dumps(res.json(), indent=4))
                print("status codes are not 200:", res_not_200)

            if res.json()['type'] == 0:
                assert True
            else:
                res_not_type.append(json.dumps(res.json()['type'], indent=4))
                print("status types are not 0:", res_not_type)

            if res.json()['ok'] == True:
                assert True
            else:
                res_not_ok.append(json.dumps(res.json()['ok'], indent=4))
                print("status ok is not true:", res_not_ok)

            if res.json()['message'] == None:
                assert True
            else:
                res_message.append(json.dumps(res.json()['message'], indent=4))
                print("status message is not none:", res_message)

            assert res.headers['Content-Type'] == 'application/json'
            assert res.reason == "OK"

            start_time = time.time()
            res = requests.post(url=self.url, json=data_list)
            end_time = time.time()
            test_time = end_time - start_time

            print(f"Response Status Code: {res.status_code}")
            print(f"Time Taken: {test_time / 1000} milliseconds")

        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(make_request, data_list)