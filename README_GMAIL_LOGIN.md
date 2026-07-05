# Gmail Login Test Suite

This test suite provides comprehensive automation tests for Gmail login functionality using Playwright and pytest.

## Test Cases Included

### 1. **test_gmail_login_valid_credentials** ✅
   - **Purpose**: Test successful Gmail login with valid credentials
   - **Steps**: Navigate to Gmail → Enter email → Click Next → Enter password → Click Next → Verify inbox loads
   - **Expected Result**: Inbox page loads successfully

### 2. **test_gmail_login_invalid_email** ❌
   - **Purpose**: Test Gmail login with invalid email format
   - **Steps**: Navigate to Gmail → Enter invalid email → Click Next
   - **Expected Result**: Error message displayed for invalid email

### 3. **test_gmail_login_invalid_password** ❌
   - **Purpose**: Test Gmail login with incorrect password
   - **Steps**: Navigate to Gmail → Enter valid email → Enter wrong password → Click Next
   - **Expected Result**: Error message displayed for invalid password

### 4. **test_gmail_login_empty_credentials** ❌
   - **Purpose**: Test Gmail login attempt without entering credentials
   - **Steps**: Navigate to Gmail → Click Next without entering email
   - **Expected Result**: Validation error displayed

### 5. **test_gmail_remember_me_option** 
   - **Purpose**: Verify "Remember me" option is available on login page
   - **Steps**: Navigate to Gmail → Enter email → Verify "Remember me" checkbox exists
   - **Expected Result**: "Remember me" option is visible

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Gmail Credentials
Set environment variables with your test Gmail account credentials:

**Windows (PowerShell):**
```powershell
$env:GMAIL_TEST_EMAIL="your-test-email@gmail.com"
$env:GMAIL_TEST_PASSWORD="your-test-password"
```

**Windows (CMD):**
```cmd
set GMAIL_TEST_EMAIL=your-test-email@gmail.com
set GMAIL_TEST_PASSWORD=your-test-password
```

**Linux/macOS:**
```bash
export GMAIL_TEST_EMAIL="your-test-email@gmail.com"
export GMAIL_TEST_PASSWORD="your-test-password"
```

### ⚠️ Security Note
- Never commit real credentials to version control
- Use test/dummy Gmail accounts for automation
- Consider using a password manager or CI/CD secrets management

## Running the Tests

### Run All Tests
```bash
pytest tests/test_gmail_login.py -v
```

### Run Specific Test
```bash
pytest tests/test_gmail_login.py::TestGmailLogin::test_gmail_login_valid_credentials -v
```

### Run with Chrome Browser (Default)
```bash
pytest tests/test_gmail_login.py -v --browser=chromium
```

### Run with Firefox Browser
```bash
pytest tests/test_gmail_login.py -v --browser=firefox
```

### Run with WebKit Browser
```bash
pytest tests/test_gmail_login.py -v --browser=webkit
```

### Run in Headless Mode (No GUI)
```bash
pytest tests/test_gmail_login.py -v --headless
```

### Run in Headless Mode with Firefox
```bash
pytest tests/test_gmail_login.py -v --browser=firefox --headless
```

### Run with Coverage Report
```bash
pytest tests/test_gmail_login.py -v --cov=tests
```

### Run with HTML Report
```bash
pytest tests/test_gmail_login.py -v --html=report.html --self-contained-html
```

## Test Markers

The tests use pytest markers for organization:

- `@pytest.mark.integration` - Tests that interact with Gmail web application
- `@pytest.mark.regression` - Regression tests for existing functionality

### Run Tests by Marker
```bash
# Run only integration tests
pytest tests/test_gmail_login.py -v -m integration

# Run only regression tests
pytest tests/test_gmail_login.py -v -m regression
```

## Test Structure

```
tests/
├── test_gmail_login.py          # Gmail login test suite
├── conftest.py                  # Shared fixtures and configuration
├── test_sample.py               # Sample tests
└── testing1.py
```

## Fixtures Available

### `page`
Provides a Playwright browser page instance
- Automatically sets viewport size (1280x720)
- Automatically closes browser after test
- Configurable via `--browser` CLI argument (chromium, firefox, webkit)
- Supports `--headless` flag for headless mode

### `gmail_credentials`
Provides Gmail email and password from environment variables
- `GMAIL_TEST_EMAIL` - Test Gmail account email
- `GMAIL_TEST_PASSWORD` - Test Gmail account password
- Skips tests if credentials not configured

### `logger`
Provides a logger instance for test logging
- Automatically logs test start/completion

### `sample_data`
Provides sample test data (username, email, password)

## Troubleshooting

### Issue: Playwright Browsers Not Installed
**Solution**: Install Playwright browsers after installing the package
```bash
playwright install
```
or install specific browser:
```bash
playwright install chromium
playwright install firefox
playwright install webkit
```

### Issue: Tests Timeout
**Solution**: Increase wait time in test or verify Gmail URL accessibility

### Issue: "Credentials Not Configured" Skip Message
**Solution**: Set environment variables:
```bash
$env:GMAIL_TEST_EMAIL="test@gmail.com"
$env:GMAIL_TEST_PASSWORD="password"
```

### Issue: Chrome/Firefox Not Installed
**Solution**: Install the browser or use the webdriver-manager which handles driver downloads

## Best Practices

1. **Use Test Accounts**: Never use production Gmail accounts
2. **Enable 2FA Bypass**: Use App Passwords instead of regular password for 2FA-enabled accounts
3. **Handle Dynamic Elements**: Gmail elements may change - update selectors if tests fail
4. **Screenshots on Failure**: Tests capture screenshots on failure in the current directory
5. **Parallel Testing**: Use `pytest-xdist` for parallel test execution:
   ```bash
   pytest tests/test_gmail_login.py -n auto
   ```

## Advanced Configuration

### Custom Waits
Modify wait times in test methods:
```python
page.wait_for_selector(selector, timeout=20000)  # 20 second timeout (in ms)
```

### Headless Mode
Run browser without GUI:
```bash
pytest tests/test_gmail_login.py -v --headless
```

### Custom Browser Launch Options
Edit `conftest.py` `page` fixture to add launch options:
```python
browser = playwright.chromium.launch(
    headless=True,
    args=["--disable-blink-features=AutomationControlled"]
)
```

## Requirements
- Python 3.7+
- Playwright 1.40.0+
- pytest 7.4.3+
- Chrome, Firefox, or Safari browser (Playwright handles installation)

## Notes
- Tests may fail if Gmail implements new UI changes or CAPTCHAs
- Two-factor authentication may block automated login
- Consider using Gmail App Passwords for accounts with 2FA enabled
- Screenshots are saved on test failure for debugging
- Playwright provides excellent cross-browser support (Chromium, Firefox, WebKit)
- Playwright automatically installs browser binaries upon first run
