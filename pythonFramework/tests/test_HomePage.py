# Invoking Browser and performing some basic actions
import time
import pytest
from Utilities.baseClass import baseClass
from pageObjects.homePage import homePage
from testData.homePageData import homePageDataset


class TestHomePage(baseClass):
    def test_homePage(self, getData):
        log = self.getLogger()
        homePageObj = homePage(self.driver)
        # Inspecting HTML elements using selenium
        log.info("First name is " + getData["firstName"])
        homePageObj.UserName().send_keys(getData["firstName"])
        homePageObj.Email().send_keys(getData["email"])
        homePageObj.Password().send_keys(getData["password"])
        homePageObj.checkbox().click()
        self.selectOptionDropDown(homePageObj.getGender(), getData["gender"])
        homePageObj.submitBtnClick().click()
        assert "Success" in homePageObj.alertMsg().text
        # This is used for wait
        time.sleep(2)
        # Refresh the browser before filling form with new dataset
        self.driver.refresh()

        # Initializing fixtures to pass three different datasets to fill the form
        # We use tuple technique here to pass the params. Tuple is used only if you want to pass values directly with indexes.
        # params=[("Zuni", "zuni@gmail.com", "123", "Female"), ("Afaq", "afaq@gmail.com", "456", "Male"), ("Harsa", "harsa@gmail.com", "7654", "Female")]
        # Another method to pass values is using dictionary. In dictionary values are stored with key
        # params = [{"firstName": "Zuni", "email": "zuni@gmail.com", "password": "123", "gender": "Female"}, {"firstName": "Afaq", "email": "afaq@gmail.com", "password": "456", "gender": "Male"}]
        # We can pass these values from seperate class
    @pytest.fixture(params=homePageDataset.getTestData("Testcase5"))
    def getData(self, request):
        return request.param
