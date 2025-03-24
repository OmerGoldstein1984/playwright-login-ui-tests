from random import random

from pages.BasePage import base_page

class NewAccountInfo_page(base_page):
    ACCOUNT_INFO_TEXT="//b[text()='Enter Account Information']"
    MR = "input[value='Mr']"
    MRs = "input[value='Mrs']"
    NAME = "#name"
    EMAIL= "#email"
    PASSWORD = "#password"
    DATE_OF_BIRTH_DAY = "select[name='days']"
    DATE_OF_BIRTH_MONTH = "select[name='months']"
    DATE_OF_BIRTH_YEAR = "select[name='years']"
    FIRST_NAME = "#first_name"
    LAST_NAME = "#last_name"
    ADDRESS = "#address1"
    COUNTRY = "#country"
    STATE = "#state"
    CITY= "#city"
    ZIP_CODE = "#zipcode"
    MOBILE_NUMBER = "#mobile_number"
    CREATE_ACCOUNT_BTN = "//button[text()='Create Account']"

    def register(self,gender,day,month,year,first_name,last_name,address,state,city,zip_code,mobile_number):
        if gender == "Mr":
            self.click(self.MR)
        else:
            self.click(self.MRs)
        self.fill(self.DATE_OF_BIRTH_DAY,day)
        self.fill(self.DATE_OF_BIRTH_MONTH,month)
        self.fill(self.DATE_OF_BIRTH_YEAR,year)
        self.fill(self.FIRST_NAME,first_name)
        self.fill(self.LAST_NAME,last_name)
        self.fill(self.ADDRESS,address)
        country_options = self.page.query_selector_all(self.COUNTRY)
        random_country = random.choice(country_options)
        self.page.select_option(self.COUNTRY, random_country.get_attribute("value"))
        self.fill(self.STATE,state)
        self.fill(self.CITY,city)
        self.fill(self.ZIP_CODE,zip_code)
        self.fill(self.MOBILE_NUMBER,mobile_number)
        self.click(self.CREATE_ACCOUNT_BTN)

    def verify_Page_loaded(self):
        self.wait_for_element(self.ACCOUNT_INFO_TEXT)

   

        


