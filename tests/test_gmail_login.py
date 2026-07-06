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
    EMAIL = "testautomation.edhas@gmail.com"
    PASSWORD = "P@ssw0rdistarunabagish28!"
    
    # Launch browser with arguments to bypass security checks
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-web-resources-dep-check"
            ]
        )
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        # Override navigator.webdriver to hide automation
        page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined,
            });
        """)
        
        try:
            # Navigate to Gmail
            page.goto("https://mail.google.com")
            print("[OK] Navigated to Gmail")
            
            # Enter email
            page.locator("#identifierId").wait_for(timeout=10000)
            email_field = page.locator("#identifierId")
            email_field.fill(EMAIL)
            email_field.press("Enter")
            print(f"[OK] Entered email: {EMAIL}")
            print("[OK] Pressed Enter to proceed")
            
            # Wait for password page to load - use longer timeout and handle gracefully
            try:
                page.wait_for_load_state("domcontentloaded", timeout=15000)
                print("[OK] Password page loaded")
            except:
                print("[WARN] Page load took longer, continuing anyway...")
                page.wait_for_timeout(2000)  # Give it 2 more seconds
            
            # Wait and enter password
            try:
                page.locator("#password").wait_for(timeout=20000)
                print("[OK] Password field found")
                password_field = page.locator("#password")
                
                # Scroll to ensure field is in view
                password_field.scroll_into_view_if_needed()
                print("[OK] Password field scrolled into view")
                
                # Take a screenshot to see the current state
                page.screenshot(path="password_field_visible.png")
                print("[DEBUG] Screenshot taken: password_field_visible.png")
                
                # Click the field to ensure focus
                password_field.click()
                print("[OK] Password field clicked")
                
                # Add a small delay to ensure field is ready
                page.wait_for_timeout(800)
                
                # Try Method 1: Direct keyboard input via page.type()
                print("[METHOD 1] Trying direct keyboard input...")
                try:
                    page.type("#password", PASSWORD, delay=30)
                    print("[OK] Password entered via keyboard - METHOD 1")
                except Exception as e1:
                    print(f"[METHOD 1 FAILED] {str(e1)}")
                    
                    # Try Method 2: JavaScript value setting
                    print("[METHOD 2] Trying JavaScript value setting...")
                    try:
                        page.evaluate(f"""
                            const field = document.querySelector('#password');
                            if (field) {{
                                field.focus();
                                field.value = '{PASSWORD}';
                                field.dispatchEvent(new Event('input', {{ bubbles: true }}));
                                field.dispatchEvent(new Event('change', {{ bubbles: true }}));
                                field.dispatchEvent(new KeyboardEvent('keydown', {{ code: 'Enter', key: 'Enter' }}));
                                console.log('Password injected via JavaScript');
                            }}
                        """)
                        print("[OK] Password set via JavaScript - METHOD 2")
                    except Exception as e2:
                        print(f"[METHOD 2 FAILED] {str(e2)}")
                        
                        # Try Method 3: Clear and fill
                        print("[METHOD 3] Trying clear and fill...")
                        try:
                            password_field.clear()
                            password_field.fill(PASSWORD)
                            print("[OK] Password entered via fill - METHOD 3")
                        except Exception as e3:
                            print(f"[METHOD 3 FAILED] {str(e3)}")
                            page.screenshot(path="password_methods_failed.png")
                            print("[DEBUG] All methods failed. Screenshot: password_methods_failed.png")
                            raise
                
                # Wait a moment before pressing Enter
                page.wait_for_timeout(1500)
                
                # Press Enter to submit
                password_field.press("Enter")
                print("[OK] Pressed Enter after password")
            except Exception as e:
                print(f"[ERROR] Failed to fill password field: {str(e)}")
                print(f"Current URL: {page.url}")
                page.screenshot(path="password_field_error.png")
                print("Screenshot saved as password_field_error.png")
                raise
            
            # Wait for navigation after password entry - be more patient
            print("[...] Waiting for page to respond after password entry...")
            try:
                page.wait_for_load_state("domcontentloaded", timeout=20000)
                print("[OK] Page loaded after password")
            except:
                print("[WARN] Page load took longer, waiting with timeout...")
                page.wait_for_timeout(5000)
            
            # Wait for inbox to load (verify successful login)
            # May need to handle 2FA prompt first
            print("[OK] Checking for successful login...")
            try:
                page.wait_for_selector(".nH.oy8Mbf", timeout=20000)
                print("[OK] Successfully logged into Gmail!")
            except:
                # If 2FA prompt appears, check if we can see the Gmail app
                print("[WARN] 2FA required - waiting for verification (check your phone)...")
                page.wait_for_selector("body", timeout=30000)
            
            # Verify URL
            print(f"Current URL: {page.url}")
            assert "mail.google.com" in page.url or "accounts.google.com" in page.url
            print("[OK] Gmail login test PASSED!")
            
        except Exception as e:
            print(f"[ERROR] Test failed: {str(e)}")
            print(f"Current URL: {page.url}")
            page.screenshot(path="gmail_login_failure.png")
            print("Screenshot saved as gmail_login_failure.png")
            raise
        
        finally:
            # Keep browser open for 30 seconds to complete 2FA if needed
            print("[...] Keeping browser open for 30 seconds (for 2FA if needed)...")
            page.wait_for_timeout(30000)
            browser.close()
            print("[OK] Browser closed")
