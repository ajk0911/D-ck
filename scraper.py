import requests
from bs4 import BeautifulSoup

def scrape_dack(dacktyp: str, dimension: str):
    base_url = "https://www.bilia.se/shop/dack/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Skapa sök-URL baserat på däcktyp och dimension
    query = f"{dacktyp} {dimension}".replace(" ", "+")
    search_url = f"{base_url}?q={query}"

    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # Hitta alla däckkort
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

