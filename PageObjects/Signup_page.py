from selenium.webdriver.common.by import By


class SignUp_Class:
    click_signup_XPATH = "/html[1]/body[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]"
    text_username_id = "username"
    text_password_id = "password"
    text_email_id = "email"
    text_phone_id = "phone"
    click_create_user_button_XPath = "//button[@type='submit']"
    success_message_xpath = "//div[@class='success-message']"

    def __init__(self, driver):
        self.driver = driver

    def Click_signup_button(self):
        self.driver.find_element(By.XPATH, self.click_signup_XPATH).click()

    def Enter_Username(self, username):
        self.driver.find_element(By.ID, self.text_username_id).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def Enter_Email(self, email):
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)

    def Enter_Phone(self, phone):
        self.driver.find_element(By.ID, self.text_phone_id).send_keys(phone)

    def Click_create_user(self):
        self.driver.find_element(By.XPATH, self.click_create_user_button_XPath).click()

    def Validate_User_Creation(self):
        try:
            success_msg = self.driver.find_element(By.XPATH, self.success_message_xpath).text
            return success_msg  # User created successfully
        except:
            pass
