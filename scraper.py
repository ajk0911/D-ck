import requests
from bs4 import BeautifulSoup
from typing import List, Dict

def try_api_scrape(dacktyp: str, dimension: str) -> List[Dict]:
    # Placeholder för framtida API-anrop om Bilia öppnar upp ett JSON-endpoint
    return []

def try_html_scrape(dacktyp: str, dimension: str) -> List[Dict]:
    base_url = "https://www.bilia.se/shop/dack/"
    headers = {"User-Agent": "Mozilla/5.0"}
    query = f"{dacktyp} {dimension}".replace(" ", "+")
    search_url = f"{base_url}?q={query}"

    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    for product in soup.find_all("div", class_="product-tile"):
        artikelnummer = product.get("data-partnumber")
        benamning_tag = product.find("div", class_="product-name")
        benamning = benamning_tag.text.strip() if benamning_tag else "Okänd benämning"
        if artikelnummer:
            results.append({
                "artikelnummer": artikelnummer,
                "benamning": benamning
            })
    return results

def hybrid_scrape(dacktyp: str, dimension: str) -> List[Dict]:
    result = try_api_scrape(dacktyp, dimension)
    if result:
        return result
    return try_html_scrape(dacktyp, dimension)
