from selenium.webdriver.common.by import By


class userRegistration:
    signupLogin_linkText = "Signup / Login"
    textbox_name_xpath = "//input[@name='name']"
    textbox_email_xpath = "//input[@data-qa='signup-email']"
    button_signup_xpath = "//button[@data-qa='signup-button']"
    account_infoText_xpath = "//div/h2[@class='title text-center']"

    def __init__(self,driver):
        self.driver = driver

    def signupLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.signupLogin_linkText).click()

    def setUserName(self,username):
        # self.driver.find_element(By.LINK_TEXT, self.signupLogin_linkText).click()
        self.driver.find_element(By.XPATH, self.textbox_name_xpath).send_keys(username)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)

    def click_signup(self):
        self.driver.find_element(By.XPATH,self.button_signup_xpath).click()

    def accountInfoText(self):
        innertext = self.driver.find_element(By.XPATH,self.account_infoText_xpath).text
        return innertext
