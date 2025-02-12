import json


def test_readFromJson(browser):
    with open('data/creds.json') as f:
        data = json.load(f)
        print(data)