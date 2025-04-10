# core/drivers.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

from services.logger import setup_logger

logger = setup_logger("driver")


def get_chrome_driver(headless: bool = True) -> webdriver.Chrome:
    """
    Returns a configured Chrome WebDriver instance.

    Args:
        headless (bool): Whether to run Chrome in headless mode. Defaults to True.

    Returns:
        webdriver.Chrome: An instance of Chrome WebDriver.
    """
    try:
        chrome_options = ChromeOptions()

        if headless:
            chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options,
        )

        driver.set_page_load_timeout(30)
        logger.info("[✓] Chrome WebDriver initialized successfully.")
        return driver

    except WebDriverException as e:
        logger.exception("Failed to initialize Chrome WebDriver.")
        raise e
