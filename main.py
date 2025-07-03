from fastapi import FastAPI, Query
from scraper import hybrid_scrape

app = FastAPI()

@app.get("/dack")
def get_dack(dacktyp: str = Query(...), dimension: str = Query(...)):
    resultat = hybrid_scrape(dacktyp, dimension)
    return {"resultat": resultat}
