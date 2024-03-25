# Invoking Browser and performing some basic actions
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# If we want to run the test in headless mode means the chrome will not open the test will run in the background.
chrome_options = webdriver.ChromeOptions()
# Chrome driver service
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")   # to open any URL on Chrome
driver.maximize_window()    # to do full screen of the automation test browser
driver.implicitly_wait(2)   # It is implicit wait. Its a global timeout of the script. If any element is not shown on the page, it will wait a max of 5 seconds for that to show up.
# Selecting product from the list using product name
driver.find_element(By.CSS_SELECTOR, "ul li:nth-child(2)").click()
ProductList = driver.find_elements(By.CSS_SELECTOR, "div h4")
ProductName = []
for proList in ProductList:
    if "Nokia Edge" == proList.text:
        driver.find_element(By.XPATH, "(//button[contains(text(),'Add')])[3]").click()
        break
driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()   # Checkout btn click
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()    # Again Checkout btn click
driver.find_element(By.ID, "country").send_keys("pa")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".suggestions")))
driver.find_element(By.LINK_TEXT, "Pakistan").click()
driver.find_element(By.CSS_SELECTOR, ".checkbox.checkbox-primary").click()
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg").click()
msgAlert = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text
assert "Success! Thank you" in msgAlert
# This is used for wait
time.sleep(5)
