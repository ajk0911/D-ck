from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

def scrape_tires(dacktyp, dimension):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service()
    driver = webdriver.Edge(service=service, options=options)

    try:
        url = "https://www.bilia.se/dack/"
        driver.get(url)

        wait = WebDriverWait(driver, 10)

        # Accept cookies if popup appears
        try:
            accept = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Acceptera')]")))
            accept.click()
        except:
            pass

        # Input dimension
        search_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='search']")))
        search_input.clear()
        search_input.send_keys(dimension)
        search_input.submit()

        time.sleep(3)

        # Filter by däcktyp
        filter_map = {
            "sommardäck": "Sommardäck",
            "dubbdäck": "Dubbdäck",
            "friktionsdäck": "Friktionsdäck",
            "året runt-däck": "Året runt-däck"
        }

        if dacktyp.lower() in filter_map:
            try:
                filter_button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//label[contains(., '{filter_map[dacktyp.lower()]}')]")))
                filter_button.click()
                time.sleep(2)
            except:
                pass

        # Extract product cards
        products = driver.find_elements(By.CSS_SELECTOR, ".product-card")
        results = []

        for product in products:
            try:
                name = product.find_element(By.CSS_SELECTOR, ".product-card__title").text.strip()
                article = product.get_attribute("data-product-id")
                if article and name:
                    results.append(f"Artikelnummer: {article} – {name}")
            except:
                continue

        return results

    finally:
        driver.quit()