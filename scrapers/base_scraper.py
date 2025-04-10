# scrapers/base_scraper.py

from config.drivers import get_chrome_driver
from services.file_manager import save_json


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
        # Use save_json to save the data as a JSON file
        save_json(data, filename)
        self.logger.info(f"Data saved to {filename}")

    def link_generator(self, json_data):
        """
        Generates a list of URLs based on the provided JSON data.

        :param json_data: A JSON object containing the necessary data to construct URLs.
        :return: A list of URLs.
        """
        links = []
        try:
            # Assuming json_data is a dictionary with a key 'urls' that contains a list of URL components
            """url_components = json_data.get("urls", [])
            for component in url_components:
                # Construct the URL based on the component
                # This is a simple example; adjust the logic as needed
                base_url = component.get("base_url", "")
                path = component.get("path", "")
                query_params = component.get("query_params", {})

                # Construct the full URL
                url = f"{base_url}{path}"
                if query_params:
                    query_string = "&".join(
                        [f"{key}={value}" for key, value in query_params.items()]
                    )
                    url = f"{url}?{query_string}"

                links.append(url)"""
        except Exception as e:
            # Handle exceptions, possibly logging them
            print(f"Error generating links: {e}")

        return links
