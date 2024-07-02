import requests
from concurrent.futures import ThreadPoolExecutor
import json
import time

class Test_lovs:
    url = "http://mld.dinero.local:8081/?cmd=lovs"

    def test_lovs(self):
        data_list = [
            {
                "lovs_label": "label",
                "language_code": "fr",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": 19,
                        "country_name": "Dubai"
                    },
                    {
                        "id": 12,
                        "country_name": "kuwait"
                    },
                    {
                        "id": 31,
                        "country_name": "kathar"
                    },
                    {
                        "id": 54,
                        "country_name": "oman"
                    }
                ]
            },
            {
                "lovs_label": "",
                "language_code": "",
                "field_to_be_translated": "",
                "lovs": [
                    {
                        "id": "",
                        "country_name": ""
                    },
                    {
                        "id": "",
                        "country_name": ""
                    },
                    {
                        "id": "",
                        "country_name": ""
                    },
                    {
                        "id": "",
                        "country_name": ""
                    }
                ]
            },
            {
            },
            {
                "lovs_label": "lovs",
                "language_code": "FR",
                "field_to_be_translated": "country"
            },
            {

            },
            {
                "lovs_label": "data",
                "language_code": "GR",
                "field_to_be_translated": "",
                "lovs": [
                    {
                        "id": 2,
                        "country_name": "Hyderabad"
                    },
                    {
                        "id": "3",
                        "country_name": "Kerala"
                    },
                    {
                        "id": "5",
                        "country_name": "Kochi"
                    }
                ]
            },
            {
                "lovs_label": "meta",
                "language_code": "GR",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": "3",
                        "country_name": "simla"
                    },
                    {
                        "id": "4",
                        "country_name": "ooty"
                    }
                ]
            },
            {
                "lovs_label": "test",
                "language_code": "FR",
                "lovs": [
                    {
                        "id": "1",
                        "country_name": "India"
                    },
                    {
                        "id": "2",
                        "country_name": "Israil"
                    },
                    {
                        "id": "4",
                        "country_name": "germany"
                    },
                    {
                        "id": "5",
                        "country_name": "chaina"
                    }
                ]
            },
            {
                "lovs_label": "data",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": "1",
                        "country_name": "Dubai"
                    },
                    {
                        "id": "3",
                        "country_name": "france"
                    },
                    {
                        "id": "4",
                        "country_name": "london"
                    },
                    {
                        "id": "5",
                        "country_name": "thiwan"
                    }
                ]
            },
            {
                "language_code": "meta",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": "9",
                        "country_name": "name"
                    },
                    {
                        "id": "",
                        "country_name": "country_name"
                    },
                    {
                        "id": "",
                        "country_name": "country"
                    },
                    {
                        "id": "",
                        "country_name": "count"
                    }
                ]
            },
            {
                "lovs_label": 1,
                "language_code": 2,
                "field_to_be_translated": 5,
                "lovs": [
                    {
                        "id": "ids",
                        "country_name": 2
                    },
                    {
                        "id": "lovs",
                        "country_name": 3
                    },
                    {
                        "id": "name",
                        "country_name": 4
                    },
                    {
                        "id": "country",
                        "country_name": 5
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "ovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "blanguage_code": "GR",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "cfield_to_be_translated": "country_name",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "country_name",
                "dlovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "country_name",
                "lovs": [
                    {
                        "eid": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "fcountry_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "gid": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "hcountry_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "iid": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "jcountry_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "kid": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "lcountry_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_labela": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"

                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "blanguage_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "cfield_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovsd": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "ide": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_namef": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "idg": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_nameh": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "idi": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_namej": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "idk": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_namel": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1

                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3
                    },
                    {
                        "id": 50,
                        "country_name": "Nepal"
                    }
                ]
            },
            {
                "lovs_label": "lovs_label",
                "language_code": "GR",
                "field_to_be_translated": "translation",
                "lovs": [
                    {
                        "id": 1,
                        "country_name": "Indonasia"
                    },
                    {
                        "id": 2,
                        "country_name": "Iraq"
                    },
                    {
                        "id": 3,
                        "country_name": "Bhootan"
                    },
                    {
                        "id": 50
                    }
                ]
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