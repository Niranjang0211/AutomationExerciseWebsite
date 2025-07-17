import string
import time
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
            self.logger.error("Expected and Actual title are not matching".center(60,"#"))
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
        time.sleep(2)

        innertext1 = self.ur.accountInfoText()
        try:
            assert innertext1 == "ENTER ACCOUNT INFORMATION"
        except AssertionError as e:
            self.logger.error(f" Enter Account Information page is not visible , {e}".center(60,"#"))
            raise
        print(innertext1)
        time.sleep(2)

        self.ur.selectTitleRadio()
        self.ur.setPassword("Epiplex@123")
        self.ur.DOBSelectDay("2")
        self.ur.DOBSelectMonth("November")
        self.ur.DOBSelectYear("1996")
        self.ur.newsCheckBox()
        self.ur.setFirstname("Vishal")
        self.ur.setlName("Rotti")
        self.ur.setCompany("TestCompany")
        self.ur.setAddress("MG Road")
        self.ur.setAddress2("Trinity")
        self.ur.selectDropdownCountry("India")
        self.ur.setState("Karnataka")
        self.ur.setCity("Dharwad")
        self.ur.setZipcode("582355")
        self.ur.setMobileno("87987798779")
        time.sleep(2)
        self.ur.createAccountBtn()
        time.sleep(2)

        try:
            assert self.ur.accountCreated() == "Account Created!".upper()
        except AssertionError as e:
            self.logger.error(f"The account is not created, cross verify it {e}")
            raise
        self.ur.clickContinue()
        try:
            assert self.ur.loggedUser() ==  "Logged in as Niranjan"
        except AssertionError as e:
            self.logger.error("Wrong user logged")
            raise
        self.ur.deleteAccount()
        try:
            assert self.ur.deleteAccountMsg() == "Account Deleted!".upper()
        except AssertionError as e:
            self.logger.error(f"Account is not deleted {e}")
            raise
        time.sleep(3)
