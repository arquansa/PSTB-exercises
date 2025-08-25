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
        "name": "Text Summarizer",
        "description": "Résumé d’un texte long en 3 phrases max.",
        "version": "1.0"
    }

@app.post("/infer")
async def infer(request: Request):
    data = await request.json()
    input_text = data.get("input", "")

    # Résumé simple : on ne prend que les 2 premières phrases.
    summary = " ".join(input_text.split(".")[:2]) + "."

    return JSONResponse(content={"output": summary})
