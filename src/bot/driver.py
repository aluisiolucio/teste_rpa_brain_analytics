from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def get_chrome_driver():
    service = Service(ChromeDriverManager().install())

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")

    return webdriver.Chrome(service=service, options=chrome_options)
