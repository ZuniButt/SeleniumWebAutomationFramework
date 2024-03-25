# Whatever the fixtures are written in this file they will be available in every test file.
import pytest


@pytest.fixture(scope="class")
def browserInvoke():
    print("Chrome is open")     # In real time, you will use this particular block to invoke browser or to invoke some configuration properties.
    yield
    print("Chrome is close")    # you will use this to close the browser and to delete the cookies at the end after your test case execution is done.


@pytest.fixture()   # This fixture is used for load data
def loadData():
    print("Data is loaded successfully")
    return ["Zuni", "Butt", "12345", "zuni@gmail.com"]


# If we run the particular test with different data multiple times. First time the test will run on chrome, second time the test will run on edge etc.
@pytest.fixture(params=["Chrome", "Edge", "Internet Explorer"])
def crossBrowser(request):
    return request.param


# If we want to send the multiple values in the one single run.
@pytest.fixture(params=[("Zuni", "Butt"),("Ali", "Butt"), "Internet"])
def userInfo(request):
    return request.param

