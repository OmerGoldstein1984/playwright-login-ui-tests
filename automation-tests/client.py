import json


def test_readFromJson(browser):
    with open('data/creds.json') as f:
        data = json.load(f)
        print(data["test"])

   # browser.goto('https://rahulshettyacademy.com/client/')
    # Iampil1984
    #browser.locator('#userEmail').fill('omergld@gmail.com')
    #browser.locator('#userPassword').fill('Iampil1984')
    #browser.locator('#login').click()