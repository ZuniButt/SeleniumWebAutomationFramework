import pytest
from selenium import webdriver

# Initializing Global variable of driver
driver = None

# If I want to invoke my browser using command line at run time then I have to clear here by writing code that I'm going to make Cmd line execution for this following code to follow
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: type1 or type2"
    )


@pytest.fixture(scope="class")
def setUp(request):
    # Now apply global variable of driver here
    global driver
    # Now get the option value "browser_name"
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()     # Default to Chrome if browser is not specified

    driver.get("https://rahulshettyacademy.com/angularpractice/")  # Open any URL in Chrome
    driver.maximize_window()
    request.cls.driver = driver # Instead returning the driver use this code
    yield
    driver.close()

# Code for Custom Report Generation with Failure tests screenshots

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
