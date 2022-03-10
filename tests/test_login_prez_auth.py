import pytest
import libraries.common as common
import libraries.library_form_authentication as auth


testdata = [
    ("trialuser0903.noreply@prezent.ai", "kiqjemkh", True),
    # ("wronguser@mailinator.com", "wrong_passowrd", False),
]
@pytest.mark.sanity_test
@pytest.mark.login_prez_test
@pytest.mark.parametrize("username, password, expected",testdata)
def test_login_to_form(username, password, expected, open_browser):
    driver = open_browser
    common.navigate_url(driver, "https://prezent-livestaging.myprezent.com/signin")
    auth.type_username(driver, username)
    auth.click_continue(driver)
    auth.type_password(driver, password)
    auth.click_login_button(driver)
    # assert auth.verify_login(driver) == expected
    auth.click_profile_icon(driver)
