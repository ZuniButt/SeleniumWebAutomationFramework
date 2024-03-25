import pytest

from pytestsDemo.loggingParent import loggingParentClass


@pytest.mark.usefixtures("browserInvoke")
@pytest.mark.usefixtures("loadData")
@pytest.mark.usefixtures("crossBrowser")
@pytest.mark.usefixtures("userInfo")
class TestExample (loggingParentClass):

    def test_secondDemo(self, loadData):   # Here this function is act as test 1
        msg = "Hi"
        assert msg == "Hi", "Failed because string do not match"   # If you want to add assertion msg after making assertion put comma and add msg.
        log = self.getLogger()
        log.info(loadData[0])
        log.info(loadData[2])


    def test_CreditCard2(self):   # Here this function is act as test 1
        value1 = 5
        assert value1+2 == 7, "Addition results does not match."

    def test_SignOut(self, crossBrowser):
        print("Its Sign out Test Case")

    def test_Signin(self, userInfo):
        print(userInfo[0])

