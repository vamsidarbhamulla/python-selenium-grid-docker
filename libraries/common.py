import allure


@allure.step
def navigate_url(driver, url):
    driver.get(url)


@allure.step
def message(content, title = "Custom Message"):
    allure.attach(content, title, allure.attachment_type.TEXT)


@allure.step
def screenshot(driver, title="Screenshot"):
    allure.attach(driver.get_screenshot_as_png(),
                  name=title,
                  attachment_type=allure.attachment_type.PNG)