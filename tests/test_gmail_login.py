"""
Simple Gmail login test using Playwright
"""

import pytest
from playwright.sync_api import sync_playwright


def test_gmail_login():
    """
    Test Gmail login with valid credentials
    """
    # Gmail credentials
    EMAIL = "anshu.sood5@gmail.com"
    PASSWORD = "P@ssw0rdistarunabagish28!"
    
    # Launch browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        try:
            # Navigate to Gmail
            page.goto("https://mail.google.com")
            print("✓ Navigated to Gmail")
            
            # Enter email
            page.locator("#identifierId").wait_for(timeout=10000)
            page.locator("#identifierId").fill(EMAIL)
            print(f"✓ Entered email: {EMAIL}")
            
            # Click Next button
            page.locator("#identifierNext").click()
            print("✓ Clicked Next button to proceed")
            
            # Wait and enter password
            page.locator("#password").wait_for(timeout=10000)
            page.locator("#password").fill(PASSWORD)
            print("✓ Entered password")
            
            # Click password Next button
            page.locator("#passwordNext").click()
            print("✓ Clicked password Next button")
            
            # Wait for inbox to load (verify successful login)
            page.wait_for_selector(".nH.oy8Mbf", timeout=20000)
            print("✓ Successfully logged into Gmail!")
            
            # Verify URL
            assert "mail.google.com" in page.url
            print("✓ Gmail login test PASSED!")
            
        except Exception as e:
            print(f"✗ Test failed: {str(e)}")
            page.screenshot(path="gmail_login_failure.png")
            raise
        
        finally:
            browser.close()
            print("browser closed")
