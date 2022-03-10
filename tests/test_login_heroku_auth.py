import pytest
import libraries.common as common
import libraries.library_form_authentication as auth


testdata = [
    ("tomsmith", "SuperSecretPassword!", True),
    ("wronguser", "wrong_passowrd", False),
]
@pytest.mark.sanity_test
@pytest.mark.login_heroku_test
@pytest.mark.parametrize("username, password, expected",testdata)
def test_login_to_form(username, password, expected, open_browser):
    driver = open_browser
    common.navigate_url(driver, "http://the-internet.herokuapp.com/login")
    auth.type_username(driver, username)
    auth.type_password(driver, password)
    auth.click_login(driver)
    assert auth.verify_login(driver) == expected

