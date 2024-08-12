import time

import pytest

from PageObjects.Login_Page import Login_Class
from PageObjects.Signup_page import SignUp_Class
from utilities.Logger import Log_Class
from utilities.readConfig import ReadConfigfile


class Test_User_login:
    User = ReadConfigfile.GetUser()
    Pass = ReadConfigfile.GetPass()
    Log = Log_Class.log_generator()

    @pytest.mark.sanity
    @pytest.mark.group1
    def test_Bank_url001(self, setup):
        self.Log.info("Testcase test_BankApp_Url is started")
        self.driver = setup
        self.Log.info("Opening browser")
        self.Log.info("Checking page title")
        if self.driver.title == "Bank Application":
            self.Log.info("Taking screenshot for test pass")
            self.driver.save_screenshot(".\\Screenshots\\test_Bank_url_pass.png")
            self.Log.info("Test for url pass")

            assert True
        else:
            self.Log.info("Take screenshot for test fail")
            self.driver.save_screenshot(".\\Screenshots\\test_Bank_url_fail.png")
            self.Log.info("Test for url fail")

            assert False

    @pytest.mark.sanity
    @pytest.mark.group1
    def test_login002(self, setup):
        self.Log.info("Opening browser")
        self.driver = setup
        self.Log.info("Import login class as lp")
        self.driver.lp = Login_Class(self.driver)
        time.sleep(2)
        self.Log.info("Click login link")
        self.driver.lp.Click_Login_Link()
        self.Log.info("Enter username")
        self.driver.lp.Enter_Username(self.User)
        self.Log.info("Enter password")
        self.driver.lp.Enter_Password(self.Pass)
        time.sleep(4)
        self.Log.info("Click on login button")
        self.driver.lp.Click_Login_Button()
        time.sleep(10)
        # self.driver.lp.click_logout_button_css()
        self.Log.info("Check for driver title")
        if self.driver.title == "Dashboard":
            self.Log.info("Test for login pass")
            assert True
        else:
            self.Log.info("Take screenshot for test fail")
            self.driver.save_screenshot(".\\Screenshots\\test_login_fail.png")
            self.Log.info("Test for login fail")
            assert False

    @pytest.mark.sanity
    @pytest.mark.group1
    def test_bank_signup003(self,generate_random_password , setup):
        self.Log.info("Opening browser")
        self.driver = setup
        self.Log.info("Import Signup class as su")
        self.Su = SignUp_Class(self.driver)
        time.sleep(2)
        self.Log.info("Click on signup button")
        self.Su.Click_signup_button()
        self.Log.info("Enter random username")
        self.Su.Enter_Username(generate_random_password())
        time.sleep(2)
        self.Log.info("Enter random password")
        self.Su.Enter_Password(generate_random_password())
        time.sleep(2)
        self.Log.info("Enter random email")
        self.Su.Enter_Email(generate_random_password())
        time.sleep(2)
        self.Log.info("Enter random phone")
        self.Su.Enter_Phone(generate_random_password())
        self.Log.info("scroll window")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self.Log.info("Click on create user")
        self.Su.Click_create_user()
        time.sleep(10)
        self.Log.info("Check for user creation")
        if self.Su.Validate_User_Creation() == "User created Successfully":
            self.Log.info("Take screenshot for test pass")
            self.driver.save_screenshot(".\\Screenshots\\test_bank_signup_pass.png")
            self.Log.info("Test for sign up pass")
            assert True
        else:
            self.Log.info("Take screenshot for test fail")
            self.driver.save_screenshot(".\\Screenshots\\test_bank_signup_fail.png")
            self.Log.info("Test for Signup fail")
            assert False

# def generate_random_username(length=6):
#     return 'User{0}'.format(''.join(random.choice(string.ascii_letters + string.digits, k=length))
#
#
# def generate_random_email(domain="gmail.com"):
#     return generate_random_username() + "@" + domain
#
#
# def generate_random_phone_number():
#     return ''.join(random.choices(string.digits, k=10))
