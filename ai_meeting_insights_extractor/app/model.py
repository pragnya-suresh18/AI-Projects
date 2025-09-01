from typing import List
from transformers import pipeline
import re

_textgen = None
_task = None
_model = None

def _load_pipeline(model_name: str):
    """
    Use 'summarization' for BART/PEGASUS; fall back to text2text for T5.
    """
    global _textgen, _task, _model
    if _textgen is not None and _model == model_name:
        return _textgen, _task
    if any(k in model_name.lower() for k in ["bart", "pegasus"]):
        _task = "summarization"
    else:
        _task = "text2text-generation"
    _textgen = pipeline(_task, model=model_name)
    _model = model_name
    return _textgen, _task

def _prompt_for_t5(chunk: str, bullets: int) -> str:
    return (
        "You are an AI meeting assistant. Write a concise summary of the meeting "
        f"in {bullets} bullet points focusing on DECISIONS, RISKS, and ACTION ITEMS.\n\n"
        f"MEETING TRANSCRIPT:\n{chunk}\n\n"
        "SUMMARY BULLETS:\n-"
    )

def _split_bullets(text: str) -> List[str]:
    parts = [re.sub(r"^[\-\*\u2022]\s*", "", ln).strip()
             for ln in re.split(r"\n+|(?:\s*\-\s*)", text)]
    return [p for p in parts if p]

def _dedup_and_filter(bullets: List[str]) -> List[str]:
    clean, seen = [], set()
    for b in bullets:
        b = re.sub(r"\s+", " ", b).strip(" -•*")
        if not b:
            continue
        # drop pathological repetitions like "Dave, Dave, Dave..."
        tokens = re.findall(r"[A-Za-z]+", b)
        if tokens and (len(set(tokens)) / max(1, len(tokens))) < 0.25:
            continue
        # drop lines that are just names
        if re.fullmatch(r"(?:[A-Z][a-z]+(?:,\s*|\s+))*[A-Z][a-z]+\.?", b):
            continue
        key = b.lower()
        if key not in seen:
            clean.append(b)
            seen.add(key)
    return clean

def summarize_chunks(chunks: List[str], bullets: int = 5,
                     model_name: str = "facebook/bart-large-cnn") -> List[str]:
    """
    Summarize each chunk, then merge and clean. Defaults to BART
    (more stable than small T5 for meetings).
    """
    gen, task = _load_pipeline(model_name)

    partials = []
    for ch in chunks:
        if task == "summarization":
            out = gen(ch, max_length=220, min_length=60, no_repeat_ngram_size=3)[0]["summary_text"]
        else:
            prompt = _prompt_for_t5(ch, bullets)
            out = gen(prompt, max_new_tokens=220, num_beams=4,
                      no_repeat_ngram_size=3, repetition_penalty=1.8)[0]["generated_text"]
        partials.append(out)

    merged = "\n".join(partials)
    if task == "summarization":
        final_text = gen(merged, max_length=240, min_length=60, no_repeat_ngram_size=3)[0]["summary_text"]
    else:
        prompt2 = (
            "Merge and deduplicate the following bullet points into a final list of "
            f"exactly {bullets} crisp bullets focusing on decisions, risks, and action items.\n\n"
            f"{merged}\n\nFINAL BULLETS:\n-"
        )
        final_text = gen(prompt2, max_new_tokens=240, num_beams=4,
                         no_repeat_ngram_size=3, repetition_penalty=1.8)[0]["generated_text"]

    bullets_out = _split_bullets(final_text)
    bullets_out = _dedup_and_filter(bullets_out)
    return bullets_out[:bullets] if len(bullets_out) > bullets else bullets_out
def get_generator(model_name: str = "google/flan-t5-base"):
    """
    Return a text2text generator for Q&A.
    If the selected summary model is a 'summarization' model (e.g., BART/PEGASUS),
    we override to a text2text model suitable for Q&A (Flan-T5).
    """
    use_name = model_name
    if any(k in model_name.lower() for k in ["bart", "pegasus"]):
        use_name = "google/flan-t5-base"  # stable text2text for Q&A

    return pipeline("text2text-generation", model=use_name)