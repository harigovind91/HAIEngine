from fastapi import FastAPI
from .engine import HAIEngine
from .security import apply_guardrails

app = FastAPI(title="HAI-Sentinel API")
engine = HAIEngine()

@app.get("/ask")
def ask_ai(query: str):
    safe_query = apply_guardrails(query)
    if "Security Alert" in safe_query:
        return {"answer": safe_query, "sources": []}
    answer, sources = engine.get_response(safe_query)
    return {"answer": answer, "sources": [str(s.metadata) for s in sources]}
