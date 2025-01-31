from time import sleep

from playwright.async_api import async_playwright, expect

def test_example(browser):
    page=browser.new_page()
    page.goto('http://www.google.com')
    print(f"\n{page.title()}")
    page.close()

def test_login_rahulshuttyacademy(browser):
     page=browser.new_page()
     page.goto('https://rahulshettyacademy.com/loginpagePractise/')
     page.get_by_label('username:').fill('rahulshettyacademy')
     page.get_by_label('password:').fill('learnin')
     page.get_by_role('combobox').select_option('teach')
     page.get_by_role('link',name="terms and conditions").click()
     page.get_by_role('button',name='Sign In').click()
     page.locator('.alert-danger').wait_for(state="visible")

     alert_text = page.locator('.alert-danger').text_content()
     print("Alert Text:", alert_text)
     assert page.locator('.alert-danger').text_content() == alert_text
     page.close()

def test_selectAndCheckout(browser):
    products=['iphone X','Blackberry']
    browser.goto('https://rahulshettyacademy.com/loginpagePractise/')
    browser.get_by_label('username:').fill('rahulshettyacademy')
    browser.get_by_label('password:').fill('learning')
    browser.get_by_role('combobox').select_option('teach')
    browser.get_by_role('link', name="terms and conditions").click()
    browser.get_by_role('button', name='Sign In').click()
    for product in products:
       prodductContainer= browser.locator('.card').filter(has_text=product)
       btn = prodductContainer.get_by_role('button')
       btn.click()
    checkoutBtn= browser.locator('.btn').filter(has_text=' Checkout ( 2 ) ')
    checkoutBtn.click()
    sleep(5)

