import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.selenium
def test_dashboard_admin_login(live_server, db_fixture_setup, chrome_browser_instance):

    browser = chrome_browser_instance

    browser.get(("%s%s" % (live_server.url, "/admin/login")))

    username = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.XPATH, "//input[@value='Log in']")

    username.send_keys("admin")
    password.send_keys("admin")
    submit.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source
