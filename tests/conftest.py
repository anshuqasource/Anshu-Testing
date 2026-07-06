"""
Pytest configuration and shared fixtures
"""

import pytest
import logging
from datetime import datetime
from playwright.sync_api import sync_playwright


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


@pytest.fixture(scope="session")
def session_config():
    """Provide session-level configuration"""
    config = {
        "timestamp": datetime.now().isoformat(),
        "test_environment": "local"
    }
    return config


@pytest.fixture(scope="function")
def logger():
    """Provide a logger for tests"""
    return logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def test_logger(request):
    """Automatically log test names"""
    logger = logging.getLogger(__name__)
    logger.info(f"Starting test: {request.node.name}")
    yield
    logger.info(f"Completed test: {request.node.name}")


@pytest.fixture
def sample_data():
    """Provide sample test data"""
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "test123456"
    }


def pytest_configure(config):
    """Pytest plugin hook for configuration"""
    config.addinivalue_line(
        "markers", "custom: marks tests as custom"
    )


@pytest.fixture
def page(request):
    """
    Provide a Playwright browser page instance
    
    Can be configured via command line:
    pytest --browser=chromium  (default)
    pytest --browser=firefox
    pytest --browser=webkit
    """
    browser_name = request.config.getoption("--browser", default="chromium")
    headless = request.config.getoption("--headless", default=False)
    
    logger = logging.getLogger(__name__)
    logger.info(f"Initializing {browser_name} browser (headless={headless})")
    
    playwright = sync_playwright().start()
    
    if browser_name.lower() == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    elif browser_name.lower() == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    else:  # chromium (default)
        browser = playwright.chromium.launch(headless=headless)
    
    page = browser.new_page()
    page.set_viewport_size({"width": 1280, "height": 720})
    
    yield page
    
    # Teardown
    logger.info("Closing browser")
    page.close()
    browser.close()
    playwright.stop()


def pytest_addoption(parser):
    """Add custom command line options"""
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser to use for testing: chromium, firefox, or webkit"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browser in headless mode"
    )
