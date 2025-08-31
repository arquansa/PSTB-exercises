from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class MCPInput(BaseModel):
    input: str

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/metadata")
def metadata():
    return {
        "tools": [  # Changement ici pour correspondre à l’architecture multi-outils
            {
                "name": "summarizer",
                "description": "Résumé d’un texte long en 3 phrases max."
            }
        ]
    }

@app.post("/infer/summarizer")  # Changement ici aussi
async def infer_summarizer(request: Request):
    data = await request.json()
    input_text = data.get("input", "")

    # Résumé simple : on ne prend que les 2 premières phrases.
    summary = " ".join(input_text.split(".")[:2]).strip() + "."

    return JSONResponse(content={"output": summary})

