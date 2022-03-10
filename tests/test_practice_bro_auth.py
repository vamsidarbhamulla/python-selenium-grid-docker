import pytest
import libraries.common as common
import libraries.library_form_authentication as auth


testdata = [
    ("typescriptuser@mailinator.com", "Typ3$crip1", True),
    ("wronguser@mailinator.com", "wrong_passowrd", False),
]
@pytest.mark.sanity_test
@pytest.mark.login_prac_test
@pytest.mark.parametrize("username, password, expected",testdata)
def test_login_to_form(username, password, expected, open_browser):
    driver = open_browser
    common.navigate_url(driver, "https://practice.automationbro.com/my-account/")
    auth.type_username(driver, username)
    auth.type_password(driver, password)
    auth.click_login(driver)
    assert auth.verify_login(driver) == expected