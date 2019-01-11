import requests
from bs4 import BeautifulSoup
from converter.constants.scraper_constants import X_RATES_CONVERTER_URL, X_RATES_RATE_DIV


def get_exchange_rate(source_currency: str, target_currency: str):
    """
    Function to scrape www.x-rates.com in order to obtain exchange rate
    source_currency: The type of currency for which conversion rate is to be obtained
    target_currency: The type of currency in which conversion rate is to be obtained
    """
    try:
        # Making request to www.x-rates.com
        page = requests.get(X_RATES_CONVERTER_URL.format(
            source_currency, target_currency, 1))

        # Scraping page
        soup = BeautifulSoup(page.text, 'html.parser')

        # Extracting and curating data from HTML <div>s from the obtained page
        conversion_rate_main = soup.find(
            class_=X_RATES_RATE_DIV).previous_sibling
        conversion_rate_trail = soup.find(
            class_=X_RATES_RATE_DIV).get_text(strip=True)
        conversion_rate = "{}{}".format(
            conversion_rate_main, conversion_rate_trail)
        conversion_rate = conversion_rate.replace(',', '')
    except Exception as exc:
        conversion_rate = None

    return float(conversion_rate)
