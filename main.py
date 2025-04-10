# main.py

from services.logger import setup_logger
from scrapers.base import run_scrapers

# Initialize the central logger
logger = setup_logger("app")


def main():
    logger.info("Application started.")

    # Run all scrapers
    run_scrapers(logger)

    logger.info("Application finished.")


if __name__ == "__main__":
    main()
