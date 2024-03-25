from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class confirmPage:
    country = (By.ID, "country")
    selectCountryfromSuggestion = (By.LINK_TEXT, "Pakistan")
    agreeTermsCheckBox = (By.CSS_SELECTOR, ".checkbox.checkbox-primary")
    purchaseBtn = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")
    successMsg = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def __init__(self, driver):
        self.driver = driver

    def countrySelect(self):
        return self.driver.find_element(*confirmPage.country)

    def selectCountryNameFromSuggestion(self):
        return self.driver.find_element(*confirmPage.selectCountryfromSuggestion)

    def agreeTermsCheckBoxClick(self):
        return self.driver.find_element(*confirmPage.agreeTermsCheckBox)

    def purchaseBtnClick(self):
        return self.driver.find_element(*confirmPage.purchaseBtn)

    def orderSuccessMsg(self):
        return self.driver.find_element(*confirmPage.successMsg)