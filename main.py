from fastapi import FastAPI, Query
from scraper import scrape_dack

app = FastAPI()

@app.get("/dack")
def get_dack(dacktyp: str = Query(...), dimension: str = Query(...)):
    resultat = scrape_dack(dacktyp, dimension)
    return {"resultat": resultat}
