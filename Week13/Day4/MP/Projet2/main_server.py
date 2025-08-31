
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import re
from textblob import TextBlob

app = FastAPI()

class MCPInput(BaseModel):
    input: str

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/metadata")
def metadata():
    return {
        "name": "Custom NLP Tools",
        "description": "Résume, nettoie du texte et détecte le sentiment",
        "tools": [
            {
                "name": "cleaner",
                "description": "Supprime les balises HTML et le bruit textuel"
            },
            {
                "name": "sentiment",
                "description": "Analyse le sentiment d’un texte (positif, négatif, neutre)"
            }
        ]
    }

@app.post("/infer/cleaner")
async def clean_text(req: Request):
    data = await req.json()
    text = data.get("input", "")
    clean = re.sub(r"<[^>]*>", "", text)  # Supprime les balises HTML
    clean = re.sub(r"\s+", " ", clean)    # Supprime les espaces inutiles
    return JSONResponse(content={"output": clean.strip()})

@app.post("/infer/sentiment")
async def analyze_sentiment(req: Request):
    data = await req.json()
    text = data.get("input", "")
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    sentiment = "positif" if polarity > 0.2 else "négatif" if polarity < -0.2 else "neutre"
    return JSONResponse(content={"output": sentiment})

