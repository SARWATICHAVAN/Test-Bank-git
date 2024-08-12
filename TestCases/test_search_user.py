import time

import pytest

from PageObjects.Login_Page import Login_Class
from PageObjects.search_user import Search_user_class
from utilities.Logger import Log_Class
from utilities.readConfig import ReadConfigfile


class Test_search_user:
    user = ReadConfigfile.GetUser()
    passw = ReadConfigfile.GetPass()
    Log = Log_Class.log_generator()

    @pytest.mark.reggretion
    @pytest.mark.group2
    def test_search_user004(self, setup):
        self.Log.info("Opening browser")
        self.driver = setup
        self.Log.info("Import login page class")
        self.lp = Login_Class(self.driver)
        self.Log.info("Click on login link")
        self.lp.Click_Login_Link()
        self.Log.info("Enter username")
        self.lp.Enter_Username(self.user)
        self.Log.info("Entering password")
        self.lp.Enter_Password(self.passw)
        self.Log.info("click on login button")

        self.lp.Click_Login_Button()
        self.Log.info("Import search user class from page objects")
        self.Su = Search_user_class(self.driver)
        self.Log.info("Click on user management")
        self.Su.Click_user_Management()
        self.Log.info("Enter username")
        self.Su.Enter_username("Tushar")
        self.Log.info("scroll window")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.Log.info("Click on search user")
        self.Su.Click_Search_User_Button()
        time.sleep(3)
        self.Log.info("Check for valid search user")
        if self.Su.Validate_Search_User() == "pass":
            self.Log.info("Test for Search user pass")
            self.driver.save_screenshot(".\\Screenshots\\test_search_user004_pass.png")

            assert True
        else:
            self.Log.info("Take screenshot for test fail")
            self.driver.save_screenshot(".\\Screenshots\\test_search_user004_fail.png")
            self.Log.info("Test for Search user fail")
            assert False
