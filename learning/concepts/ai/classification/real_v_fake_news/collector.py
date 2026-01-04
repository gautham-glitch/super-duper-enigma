import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
# Setup headers
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# Retry-enabled requests session
def get_retry_session():
    session = requests.Session()
    retry = Retry(total=3, backoff_factor=0.3)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

# Try extracting article with requests
def fetch_with_requests(link):
    session = get_retry_session()
    response = session.get(link, headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

# Fallback to Selenium if needed
def fetch_with_selenium(link):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920x1080")
    options.add_argument(f"user-agent={HEADERS['User-Agent']}")

    driver = webdriver.Chrome(options=options)
    driver.get(link)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "article"))
        )
    except Exception:
        print("Timeout waiting for <article> tag.")

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    return soup

# Flexible tag search
def extract_article_text(soup):
    article = (
        soup.find("article")
        or soup.find("div", class_="story-body")
        or soup.find("section")
    )
    if article:
        return article.get_text(separator=" ", strip=True)
    return None

# Main function
def article_find(link, verbose=True):
    try:
        soup = fetch_with_requests(link)
        text = extract_article_text(soup)
        if text:
            return text
        else:
            raise ValueError("No <article> tag found with requests.")
    except Exception as e:
        if verbose:
            print(f"Requests failed: {e}")
            print("Trying with Selenium...")

        try:
            soup = fetch_with_selenium(link)
            text = extract_article_text(soup)
            if text:
                return text
            else:
                return "No <article> tag found with Selenium either."
        except Exception as se:
            return f"Selenium failed: {se}"
