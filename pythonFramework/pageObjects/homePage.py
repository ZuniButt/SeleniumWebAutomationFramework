from selenium.webdriver.common.by import By

from pageObjects.checkOutPage import checkOutPage


class homePage:
    shop = (By.CSS_SELECTOR, "ul li:nth-child(2)")  # Create a tuple inside these brackets "()" and here shop is a class variable
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkBox = (By.ID, "exampleCheck1")
    Gender = (By.ID, "exampleFormControlSelect1")
    submitBtn = (By.XPATH, "//input[@type='submit']")
    msg = (By.CLASS_NAME, "alert-success")


    def __init__(self, driver): # This is constructor
        self.driver = driver

    def shopItems(self):
        # If you want to deserialize this tuple in a proper way of your selenium step, mark it as a star so that it understands and treat this variable as a tuple.
        self.driver.find_element(*homePage.shop).click()    # We call class variable shop and use * to treat this shop variable as a tuple.
        checkoutPageObj = checkOutPage(self.driver)
        return checkoutPageObj

    def UserName(self):
        return self.driver.find_element(*homePage.name)

    def Email(self):
        return self.driver.find_element(*homePage.email)

    def Password(self):
        return self.driver.find_element(*homePage.password)

    def checkbox(self):
        return self.driver.find_element(*homePage.checkBox)

    def getGender(self):
        return self.driver.find_element(*homePage.Gender)

    def submitBtnClick(self):
        return self.driver.find_element(*homePage.submitBtn)

    def alertMsg(self):
        return self.driver.find_element(*homePage.msg)
