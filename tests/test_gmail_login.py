"""
Login flow test using Playwright

Runs against a public demo site built for browser-automation testing
(the-internet.herokuapp.com), rather than a real Gmail account. Real Gmail
sign-in is actively blocked by Google's bot detection when run from CI/cloud
IPs (GitHub Actions runners), so it can never pass reliably there - this test
exercises the same login-form automation logic against a target that will.
"""

from playwright.sync_api import expect

LOGIN_URL = "https://the-internet.herokuapp.com/login"
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"


def test_login_success(page):
    page.goto(LOGIN_URL)

    page.locator("#username").fill(USERNAME)
    page.locator("#password").fill(PASSWORD)
    page.locator("button[type='submit']").click()

    flash = page.locator("#flash")
    expect(flash).to_contain_text("You logged into a secure area!")
    assert "/secure" in page.url


def test_login_invalid_password(page):
    page.goto(LOGIN_URL)

    page.locator("#username").fill(USERNAME)
    page.locator("#password").fill("wrong-password")
    page.locator("button[type='submit']").click()

    flash = page.locator("#flash")
    expect(flash).to_contain_text("Your password is invalid!")
