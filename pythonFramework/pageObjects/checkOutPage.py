from selenium.webdriver.common.by import By

from pageObjects.finalCheckOutCart import finalCheckOutCart


class checkOutPage:
    products = (By.CSS_SELECTOR, "div h4")
    addProductsinCart = (By.XPATH, "(//button[contains(text(),'Add')])[3]")
    checkoutBtn = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")


    def __init__(self, driver):
        self.driver = driver

    def productList(self):
        return self.driver.find_elements(*checkOutPage.products)

    def addProductinCart(self):
        return self.driver.find_element(*checkOutPage.addProductsinCart)

    def checkOutBtnClick(self):
        self.driver.find_element(*checkOutPage.checkoutBtn).click()
        finalCheckOutCartObj = finalCheckOutCart(self.driver)
        return finalCheckOutCartObj

