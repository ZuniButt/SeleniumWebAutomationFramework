import time
from Utilities.baseClass import baseClass
from pageObjects.checkOutPage import checkOutPage
from pageObjects.homePage import homePage


class Testone(baseClass):
    def test_e2e(self):

        # Getting log here
        log = self.getLogger()
        # Calling the object of the checkOutPage.py
        checkoutPageObj = homePage(self.driver).shopItems()
        self.driver.implicitly_wait(2)  # It is implicit wait. Its a global timeout of the script. If any element is not shown on the page, it will wait a max of 5 seconds for that to show up.
        # Selecting product from the list using product name
        log.info("Getting Products List")
        ProductList = checkoutPageObj.productList()
        for proList in ProductList:
            if "Nokia Edge" == proList.text:
                checkoutPageObj.addProductinCart().click()
                break
        # calling object of finalCheckOutCart.py
        finalCheckOutCartObj = checkOutPage(self.driver).checkOutBtnClick()
        # Calling object of confirmPage.py
        confirmPageObj = finalCheckOutCartObj.successCheckOutBtnClick()  # Again Checkout btn click
        log.info("Entering Country name start from pa")
        confirmPageObj.countrySelect().send_keys("pa")
        self.explicitWaitforDynamicList("Pakistan")
        confirmPageObj.selectCountryNameFromSuggestion().click()
        confirmPageObj.agreeTermsCheckBoxClick().click()
        confirmPageObj.purchaseBtnClick().click()
        msgAlert = confirmPageObj.orderSuccessMsg().text
        log.info("Confirmation msg "+msgAlert)
        assert "Success! Thank you" in msgAlert
        # This is used for wait
        time.sleep(5)
