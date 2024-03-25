import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setUp")
class baseClass:
    # Logger code
    def getLogger(self):
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        fileHandler = logging.FileHandler('logFiles\logFile.log')
        formatter = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # This is the basic market level log file format. It can be changed.
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(
            logging.DEBUG)  # set level is use to set the starting point of the logging file execution. if level is set as error then all error file and critical files will be executed and remaining two will be skipped.
        return logger

    # Write the explicit wait function here so that it is available for all tests and this way we don't need to write wait code again.
    def explicitWaitforDynamicList(self, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    # A general drop down list code
    def selectOptionDropDown(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)
