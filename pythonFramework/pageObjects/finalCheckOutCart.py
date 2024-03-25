from selenium.webdriver.common.by import By

from pageObjects.confirmPage import confirmPage


class finalCheckOutCart:
    successCheckout = (By.CSS_SELECTOR, ".btn.btn-success")

    def __init__(self, driver):
        self.driver = driver

    def successCheckOutBtnClick(self):
        self.driver.find_element(*finalCheckOutCart.successCheckout).click()
        confirmPageObj = confirmPage(self.driver)
        return confirmPageObj
