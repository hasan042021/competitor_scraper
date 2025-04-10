# scrapers/base.py

from scrapers.otto.base import OttoScraper


def run_scrapers(logger):
    # Initialize and run the Otto scraper
    otto_scraper = OttoScraper(logger)
    otto_scraper.run()
