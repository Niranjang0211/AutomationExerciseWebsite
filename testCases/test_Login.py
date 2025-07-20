import time
from selenium.common import NoSuchElementException
from PageObjects.registerUser import userRegistration
from Utilities.CustomLogger import LogGeneration
from Utilities.XLUtils import readData, getRowCount
from Utilities.readProperties import ReadConfig

class Test_002_Login:
    baseUrl=ReadConfig.getApplicationUrl()
    logger = LogGeneration.logGen()

    def test_loginWithDifferentUsers(self,setup):
        self.driver=setup
        self.driver.get(self.baseUrl)
        home_page_title = self.driver.title
        try:
            assert home_page_title == ReadConfig.getHomePageTitle()
        except:
            self.logger.error("Home Page title is not matching")
            raise
        self.ur = userRegistration(self.driver)

        self.ur.signupLogin()
        login_title =self.driver.title
        assert login_title == ReadConfig.getLoginSignupTitle()
        assert self.ur.loginText() == "Login to your account"

        filepath = r"C:\Users\niranjan.m\PycharmProjects\AutomationExerciseWebsite\AutomationExerciseWebsite\TestData\LoginData.xlsx"
        row = getRowCount(filepath,"Login")
        #print(row)
        for r in range(2,row+1):
            email = readData(filepath,"Login",r,1)
            password = readData(filepath,"Login", r,2)
            self.ur.setLoginEmail(email)
            self.ur.setLoginPassword(password)
            self.ur.clickLogin()
            time.sleep(3)
            try:
                assert self.ur.loggedUser() == "Logged in as NIranjan"
                self.logger.info(f"Login passed for : {email}")
                self.ur.clickLogout()
            except NoSuchElementException:
                self.logger.error(f"Login failed for: {email}")
                try:
                    assert self.ur.loginErrorText() == "Your email or password is incorrect!"
                    self.logger .info("Correct error message displayed for invalid credentials.")
                except:
                    self.logger.error("Error message not displayed for invalid credentials")
                continue
        time.sleep(5)
        #self.ur.deleteAccount()
     #assert self.ur.deleteAccountMsg()
        #time.sleep(4)