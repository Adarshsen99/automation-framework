import pytest
import requests
from concurrent.futures import ThreadPoolExecutor
import json
import time

class Test_label:

    url = "http://mld.dinero.local:8081/?cmd=label"

    @pytest.mark.test
    def test_label_requests(self):
        scr_id = "sid1"
        s_txt = "trasnslator"
        l_code = "ar"

        data_list = [
            {
                "screen_id": "animals",
                "source_text": "Tiger",
                "language_code": "ar"
            },
            {
                "screen_id": "",
                "source_text": "",
                "language_code": ""
            },
            {

            },
            {
                "screen_id": 1,
                "source_text": 2,
                "language_code": 3
            },

            {
                "screens_id": scr_id,
                "source_text": s_txt,
                "language_code": l_code
            },
            {
                "screen_id": scr_id,
                "sources_text": s_txt,
                "language_code": l_code
            },
            {
                "screen_id": scr_id,
                "source_text": s_txt,
                "languages_code": l_code
            },
            {
                "screen_ida": scr_id,
                "source_text": s_txt,
                "language_code": l_code
            },
            {
                "screen_id": scr_id,
                "source_textb": s_txt,
                "language_code": l_code
            },
            {
                "screen_id": scr_id,
                "source_text": s_txt,
                "language_codec": l_code
            },
            {
                "screen_id": scr_id,
                "source_text": s_txt,
                "language_code": l_code
            },
            {
                "ascreen_id": scr_id,
                "source_text": s_txt,
                "language_code": l_code
            },
            {
                "screen_id": scr_id,
                "bsource_text": s_txt,
                "language_code": l_code
            },
            {
                "screen_id": scr_id,
                "source_text": s_txt,
                "clanguage_code": l_code
            },
            {
                "creen_id": scr_id,
                "source_text": s_txt,
                "language_code": l_code
            },
            {
                "screen_id": scr_id,
                "source_text": s_txt,
                "language_code": l_code
            },
            {
                "screen_id": scr_id,
                "ource_text": s_txt,
                "language_code": l_code
            },
            {
                "screen_id": scr_id,
                "source_text": s_txt,
                "anguage_code": l_code
            },

            {
                "creen_id": scr_id,
                "source_text": s_txt,
                "language_code": l_code
            },
            {
                "screen_id": scr_id,
                "ource_text": s_txt,
                "language_code": l_code
            },
            {
                "screen_id": scr_id,
                "source_text": s_txt,
                "anguage_code": l_code
            },
            {
                "screen_i": scr_id,
                "source_text": s_txt,
                "language_code": l_code
            },
            {
                "screen_id": scr_id,
                "source_tex": s_txt,
                "language_code": l_code
            },
            {
                "screen_id": scr_id,
                "source_text": s_txt,
                "language_cod": l_code
            },
            {
                "screen_id": scr_id,

            },
            {

                "source_text": s_txt,

            },
            {

                "language_code": l_code
            },
            {
                "screen_id": scr_id,

                "language_code": l_code
            },
            {
                "screen_id": scr_id,
                "source_text": s_txt,

            },
            {

                "source_text": s_txt,
                "language_code": l_code
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
            print(f"Time Taken: {test_time/1000} milliseconds")

        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(make_request, data_list)