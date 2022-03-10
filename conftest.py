import pytest
import allure
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Type in browser type")
    parser.addoption("--executor", action="store", default="standalone", help="For selenium grid.")
    parser.addoption("--url", action="store", default="http://the-internet.herokuapp.com", help="url")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@allure.step("Open Browser")
@pytest.fixture(scope="function")
def open_browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")

    if executor == "local" or executor == "" or executor == "standalone":
        if browser == 'chrome':
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        if executor == "remote":
            command_executor = 'http://localhost:4444/wd/hub'
        else:
            command_executor = 'http://' + executor + '/wd/hub'  ## Expecting IP and Port. Eg. 1.1.1.1:4444

        caps = {'browserName': os.getenv('BROWSER', browser)}
        driver = webdriver.Remote(
            command_executor=command_executor,
            desired_capabilities=caps)

    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver # Teardown
    driver.close()
    driver.quit()


@pytest.fixture(autouse=True)
def allure_logs(request, open_browser):
    driver = open_browser
    yield driver
    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            driver.execute_script("document.body.bgColor = 'white';")
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass # just ignore
