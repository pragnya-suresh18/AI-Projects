from typing import List
from transformers import pipeline

_text2text = None
_current_model_name = None

def get_generator(model_name: str = "google/flan-t5-base"):
    global _text2text, _current_model_name
    if _text2text is None or _current_model_name != model_name:
        _text2text = pipeline("text2text-generation", model=model_name)
        _current_model_name = model_name
    return _text2text

def summarize_chunks(chunks: List[str], bullets: int = 5, model_name: str = "google/flan-t5-base") -> List[str]:
    gen = get_generator(model_name)
    bullet_list: List[str] = []
    partials = []
    for ch in chunks:
        prompt = f"Summarize the following meeting transcript into {bullets} concise bullet points:\n\n{ch}\n\nBullets:"
        out = gen(prompt, max_new_tokens=256, num_beams=4)[0]["generated_text"]
        partials.append(out)
    combined = "\n".join(partials)
    prompt2 = f"Merge and deduplicate these bullet points into exactly {bullets} crisp bullets:\n\n{combined}\n\nBullets:"
    out2 = gen(prompt2, max_new_tokens=256, num_beams=4)[0]["generated_text"]
    for line in out2.splitlines():
        line = line.strip("-*• \t")
        if line:
            bullet_list.append(line)
    if not bullet_list:
        bullet_list = [out2.strip()]
    return bullet_list
