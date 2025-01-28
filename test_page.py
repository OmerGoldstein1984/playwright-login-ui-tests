from time import sleep


def test_example(browser):
    page=browser.new_page()
    page.goto('http://www.google.com')
    print(f"\n{page.title()}")
    page.close()

def test_login_rahulshuttyacademy(browser):
     page=browser.new_page()
     page.goto('https://rahulshettyacademy.com/loginpagePractise/')
     page.get_by_label('username:').fill('rahulshettyacademy')
     page.get_by_label('password:').fill('learning')
     page.get_by_role('combobox').select_option('teach')
     page.locator('#terms').check()
     page.get_by_role('button',name='Sign In').click()