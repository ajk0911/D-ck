from fastapi import FastAPI, Query
from scraper import scrape_tires

app = FastAPI()

@app.get("/dack")
def get_tires(
    dacktyp: str = Query(..., description="Typ av däck, t.ex. sommardäck, dubbdäck, friktionsdäck, året runt-däck"),
    dimension: str = Query(..., description="Däckdimension, t.ex. 205/55R16")
):
    result = scrape_tires(dacktyp, dimension)
    return {"resultat": result}