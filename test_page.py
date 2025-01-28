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