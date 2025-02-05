from time import sleep
from playwright import sync_api
fakeResponse={"data":[],"message":"No Orders"}
def sendResponse(route):
    route.fulfill(
        json=fakeResponse
    )
def catchRequest(route):
    route.continue_(url='https://rahulshettyacademy.com/api/ecom/order/get-orders-details/?id=123456')
def test_network_showFakeResponse(browser):
    browser.route('https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*',sendResponse)
    browser.goto('https://rahulshettyacademy.com/client/')
    # Iampil1984
    browser.locator('#userEmail').fill('omergld@gmail.com')
    browser.locator('#userPassword').fill('Iampil1984')
    browser.locator('#login').click()
    browser.locator('button').filter(has_text='ORDERS').click()
    print(f"\n"+browser.locator('.mt-4').text_content())

def test_network_CatchRequest(browser):
    browser.route('https://rahulshettyacademy.com/api/ecom/order/get-orders-details/?id=*',catchRequest)
    browser.goto('https://rahulshettyacademy.com/client/')
    # Iampil1984
    browser.locator('#userEmail').fill('omergld@gmail.com')
    browser.locator('#userPassword').fill('Iampil1984')
    browser.locator('#login').click()
    browser.locator('button').filter(has_text='ORDERS').click()
    browser.get_by_role('button',name='View').first.click()
    sleep(10)
    print(f"\n"+browser.locator('.mt-4').text_content())


