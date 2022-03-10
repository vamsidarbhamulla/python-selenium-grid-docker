from selenium.common.exceptions import NoSuchElementException
from libraries.locators import Locators
import allure


@allure.step
def type_username(driver, username):
    driver.find_element_by_id(Locators.id_username).send_keys(username)


@allure.step
def type_password(driver, password):
    driver.find_element_by_id(Locators.id_password).send_keys(password)

@allure.step
def click_continue(driver):
    driver.find_element_by_id(Locators.id_continue_button).click()

@allure.step
def click_login(driver):
    driver.find_element_by_xpath(Locators.xpath_login_button).click()

@allure.step
def click_login_button(driver):
    driver.find_element_by_id(Locators.id_login_button).click()

@allure.step
def click_profile_icon(driver):
    driver.find_element_by_xpath(Locators.xpath_profile_icon).click()

@allure.step
def verify_prezent_login(driver):
    logged_in = False
    try:
        driver.find_element_by_xpath(Locators.class_logo)
        logged_in = True
    except NoSuchElementException:
        logged_in = False
    return logged_in

@allure.step
def verify_login(driver):
    logged_in = False
    try:
        message = driver.find_element_by_xpath(Locators.xpath_loggedin_message).text
        if "You logged into a secure area!" in message:
            logged_in = True
    except:
        pass
    return logged_in