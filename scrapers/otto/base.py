# scrapers/otto/base.py

from otto.manufacturer_scraper import ManufacturerScraper
from otto.models_scraper import ModelsScraper
from otto.products_scraper import ProductsScraper


class OttoScraper:
    def __init__(self, logger):
        # Initialize specific scrapers for the Otto domain
        self.logger = logger
        self.manufacturer_scraper = ManufacturerScraper(logger)
        self.models_scraper = ModelsScraper(logger)
        self.products_scraper = ProductsScraper(logger)

    def run(self):
        try:
            # Run each scraper
            self.logger.info("Starting manufacturer scraping...")
            manufacturer_data = self.manufacturer_scraper.scrape()
            self.logger.info("Manufacturer scraping completed.")

            self.logger.info("Starting models scraping...")
            models_data = self.models_scraper.scrape()
            self.logger.info("Models scraping completed.")

            self.logger.info("Starting products scraping...")
            products_data = self.products_scraper.scrape()
            self.logger.info("Products scraping completed.")
        finally:
            # Ensure all drivers are closed
            self.manufacturer_scraper.close()
            self.models_scraper.close()
            self.products_scraper.close()
