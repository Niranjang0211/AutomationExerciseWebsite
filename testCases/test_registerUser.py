import string
import time
from venv import logger

import pytest
import random
from Utilities.readProperties import ReadConfig
from testCases.conftest import setup
from PageObjects.registerUser import userRegistration
from Utilities.CustomLogger import LogGeneration

def randomGenerator(size=8,chrs=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chrs) for x in range(size))
print(randomGenerator()+"@gmail.com")

class Test_001_RegisterUser:
    baseUrl = ReadConfig.getApplicationUrl()
    logger = LogGeneration.logGen()

    def test_homePageTitleAndSignUpPage(self, setup):

        self.driver = setup
        self.driver.get(self.baseUrl)
        #self.logger.info(" Test_001_RegisterUser ".center(40,"*"))
        self.logger.info(" Test_001_RegisterUser ".center(60,"*"))
        self.logger.info(" Verifying Home Page Title ".center(60,"*"))
        home_page_title=self.driver.title

        try:
            assert home_page_title == "Automation Exercise"
        except:
            logger.error("Expected and Actual title are not matching".center(60,"#"))
            raise

        self.ur = userRegistration(self.driver)
        self.ur.signupLogin()
        signup_login_title = self.driver.title
        assert signup_login_title == "Automation Exercise - Signup / Login"

        self.ur.setUserName("Niranjan")

        email=randomGenerator()+"@gmail.com"
        self.ur.setEmail(email)
        self.ur.click_signup()
        signup = self.driver.title
        #assert signup=="Automation Exercise - Signup"
        time.sleep(3)

        innertext1 = self.ur.accountInfoText()
        try:
            assert innertext1 == "1234"
        except AssertionError as e:
            logger.error(f" Enter Account Information page is not visible , {e}".center(60,"#"))
        print(innertext1)
        time.sleep(6)
