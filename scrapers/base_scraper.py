# scrapers/base_scraper.py

from config.drivers import get_chrome_driver
from config.settings import INTERMEDIARY_DIR


class BaseScraper:
    def __init__(self, logger):
        # Initialize the WebDriver
        self.driver = get_chrome_driver()
        self.logger = logger
        self.logger.info("WebDriver initialized.")

    def scrape(self):
        # Placeholder for scrape method
        raise NotImplementedError("Scrape method must be implemented by subclasses.")

    def close(self):
        # Close the WebDriver
        self.driver.quit()
        self.logger.info("WebDriver closed.")

    def save_data(self, data, filename):
        # Save data to a file in the raw directory
        INTERMEDIARY_DIR.mkdir(parents=True, exist_ok=True)
        file_path = INTERMEDIARY_DIR / filename
        with open(file_path, "w") as f:
            f.write(str(data))
        self.logger.info(f"Data saved to {file_path}")
