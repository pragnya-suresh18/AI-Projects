from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .schemas import InsightsRequest, SummarizeRequest, ExtractRequest, InsightsResponse, ActionItem
from .preprocess import normalize, chunk_text
from .model import summarize_chunks
from .extract import extract_action_items

app = FastAPI(title="AI Meeting Insights Extractor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/summarize")
def summarize(req: SummarizeRequest):
    options = req.options or {}
    model_name = getattr(options, "model_name", "google/flan-t5-base")
    max_chars = getattr(options, "max_chunk_chars", 4000)
    bullets = getattr(options, "summary_bullets", 5)

    text = normalize(req.transcript)
    chunks = chunk_text(text, max_chars)
    bullets_out = summarize_chunks(chunks, bullets=bullets, model_name=model_name)
    return {"summary": bullets_out, "meta": {"chunks": len(chunks), "model_name": model_name}}

@app.post("/extract")
def extract(req: ExtractRequest):
    items = extract_action_items(req.transcript)
    return {"action_items": items, "meta": {"count": len(items)}}

@app.post("/insights", response_model=InsightsResponse)
def insights(req: InsightsRequest):
    options = req.options or {}
    model_name = getattr(options, "model_name", "google/flan-t5-base")
    max_chars = getattr(options, "max_chunk_chars", 4000)
    bullets = getattr(options, "summary_bullets", 5)

    text = normalize(req.transcript)
    chunks = chunk_text(text, max_chars)
    bullets_out = summarize_chunks(chunks, bullets=bullets, model_name=model_name)
    items = extract_action_items(text)

    return InsightsResponse(
        summary=bullets_out,
        action_items=[ActionItem(**x) for x in items],
        meta={"model_name": model_name, "chunks": len(chunks)},
    )
