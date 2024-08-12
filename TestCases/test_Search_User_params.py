import time

import pytest

from utilities.readConfig import ReadConfigfile
from PageObjects.Login_Page import Login_Class
from PageObjects.search_user import Search_user_class


class Test_Search_User_params:
    Username = ReadConfigfile.GetUser()
    Password = ReadConfigfile.GetPass()

    @pytest.mark.regression
    @pytest.mark.group2
    def test_search_user_params_005(self, setup, getDataForSearchUser):
        self.driver = setup
        self.lp = Login_Class(self.driver)
        self.lp.Click_Login_Link()
        self.lp.Enter_Username(self.Username)
        self.lp.Enter_Password(self.Password)
        self.lp.Click_Login_Button()
        self.su = Search_user_class(self.driver)
        self.su.Click_user_Management()

        Search_Username = getDataForSearchUser[0]
        print(Search_Username)
        Expected_result = getDataForSearchUser[1]
        print(Expected_result)

        self.su.Enter_username(Search_Username)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)
        self.su.Click_Search_User_Button()
        if self.su.Validate_Search_User() == "pass" and Expected_result == "pass":
            assert True
        elif self.su.Validate_Search_User() == "pass" and Expected_result == "fail":
            assert False
        elif self.su.Validate_Search_User() == "fail" and Expected_result == "pass":
            assert False
        elif self.su.Validate_Search_User() == "pass" and Expected_result == "pass":
            assert True
