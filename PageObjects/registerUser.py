from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class userRegistration:
    signupLogin_linkText = "Signup / Login"
    textbox_name_xpath = "//input[@name='name']"
    textbox_email_xpath = "//input[@data-qa='signup-email']"
    button_signup_xpath = "//button[@data-qa='signup-button']"
    account_infoText_xpath = "//div/h2[@class='title text-center']"
    title_radio_btn_id = "id_gender1"
    textbox_password_id = "password"
    DOB_dropdown_days_id = "days"
    DOB_dropdown_month_id = "months"
    DOB_dropdown_year_id = "years"
    check_newsletter_id = "newsletter"
    textbox_Firstname_id = "first_name"
    textbox_Lastname_id = "last_name"
    textbox_company_id = "company"
    textbox_address_id = "address1"
    textbox_address2_id = "address2"
    dropdown_country_id = "country"
    textbox_state_id = "state"
    textbox_city_id = "city"
    textbox_zipcode_id = "zipcode"
    textbox_mobileNumber_id = "mobile_number"
    btn_createAccount_linkText = "//*[@id='form']/div/div/div/div[1]/form/button"
    accountCreatedMSG_xpath = "//h2[@data-qa='account-created']/b"
    btnContinue_xpath = "//a[@data-qa='continue-button']"
    loggedUseName_xpath = "//ul[@class='nav navbar-nav']/li[10]"
    deleteAccount_xpath = " //a[@href='/delete_account']"
    deleteAccountMsg_xpath = "//h2[@class='title text-center']/b"

    # Login Related Locators
    loginText_xpath = "//*[@id='form']/div/div/div[1]/div/h2"
    loginEmailAddress_xpath = "//input[@data-qa='login-email']"
    loginPassword_xpath = "//input[@data-qa='login-password']"
    loginButton_xpath = "//button[@data-qa='login-button']"
    logoutButton_xpath = "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a"
    loginError_xpath = "//*[@id='form']/div/div/div[1]/div/form/p"

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

    def selectTitleRadio(self):
        self.driver.find_element(By.ID, self.title_radio_btn_id).click()

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def DOBSelectDay(self,day):
        selectDay = self.driver.find_element(By.ID,self.DOB_dropdown_days_id)
        select = Select(selectDay)
        select.select_by_visible_text(day)

    def DOBSelectMonth(self,month):
        selectMonth = self.driver.find_element(By.ID, self.DOB_dropdown_month_id)
        Select(selectMonth).select_by_visible_text(month)

    def DOBSelectYear(self,year):
        selectYear = self.driver.find_element(By.ID,self.DOB_dropdown_year_id)
        Select(selectYear).select_by_visible_text(year)

    def newsCheckBox(self):
        self.driver.find_element(By.ID,self.check_newsletter_id).click()

    def setFirstname(self,fName):
        self.driver.find_element(By.ID,self.textbox_Firstname_id).send_keys(fName)

    def setlName(self,lName):
        self.driver.find_element(By.ID, self.textbox_Lastname_id).send_keys(lName)

    def setCompany(self,company):
        self.driver.find_element(By.ID, self.textbox_company_id).send_keys(company)

    def setAddress(self,address):
        self.driver.find_element(By.ID, self.textbox_address_id).send_keys(address)

    def setAddress2(self,address2):
        self.driver.find_element(By.ID, self.textbox_address2_id).send_keys(address2)

    def selectDropdownCountry(self,country):
        selectCountry = self.driver.find_element(By.ID,self.dropdown_country_id)
        Select(selectCountry).select_by_visible_text(country)

    def setState(self,state):
        self.driver.find_element(By.ID,self.textbox_state_id).send_keys(state)

    def setCity(self,city):
        self.driver.find_element(By.ID,self.textbox_city_id).send_keys(city)

    def setZipcode(self,zipcode):
        self.driver.find_element(By.ID,self.textbox_zipcode_id).send_keys(zipcode)

    def setMobileno(self,mobile):
        self.driver.find_element(By.ID,self.textbox_mobileNumber_id).send_keys(mobile)

    def createAccountBtn(self):
        self.driver.find_element(By.XPATH,self.btn_createAccount_linkText).click()

    def accountCreated(self):
        accountCreatedMSG = self.driver.find_element(By.XPATH, self.accountCreatedMSG_xpath).text
        return accountCreatedMSG

    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.btnContinue_xpath).click()

    def loggedUser(self):
        username = self.driver.find_element(By.XPATH,self.loggedUseName_xpath).text
        return username

    def deleteAccount(self):
        self.driver.find_element(By.XPATH, self.deleteAccount_xpath).click()

    def deleteAccountMsg(self):
        return self.driver.find_element(By.XPATH, self.deleteAccountMsg_xpath).text

    #Log in related methods
    def loginText(self):
       return self.driver.find_element(By.XPATH,self.loginText_xpath).text

    def setLoginEmail(self,email):
        self.driver.find_element(By.XPATH,self.loginEmailAddress_xpath).send_keys(email)

    def setLoginPassword(self,password):
        self.driver.find_element(By.XPATH,self.loginPassword_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.loginButton_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.logoutButton_xpath).click()

    def loginErrorText(self):
        return self.driver.find_element(By.XPATH,self.loginError_xpath).text
