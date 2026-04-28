import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BaseScraper:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        # Add headers to mimic a common browser and prevent immediate blocking
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/120.0.0.0 Safari/537.36'
        })
        
    def fetch_page(self, url: str) -> str:
        """Fetches the HTML content of the provided URL."""
        try:
            logger.info(f"Fetching: {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return ""

    def parse_html(self, html: str) -> BeautifulSoup:
        """Parses the HTML content into a BeautifulSoup object."""
        if not html:
            return None
        return BeautifulSoup(html, 'lxml')

if __name__ == "__main__":
    # Example usage
    scraper = BaseScraper("https://example.com")
    html = scraper.fetch_page("https://example.com")
    if html:
        soup = scraper.parse_html(html)
        logger.info(f"Page title: {soup.title.string}")
