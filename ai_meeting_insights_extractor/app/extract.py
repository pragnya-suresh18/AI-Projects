# app/extract.py
import re
from typing import List, Dict, Any
from .preprocess import get_nlp, split_by_speaker

ACTION_PATTERNS = [
    r"\bI['’]ll\b", r"\bI will\b", r"\bwe will\b",
    r"\bwe need to\b", r"\bneed to\b",
    r"\bplease\b", r"\bwill\b",
    r"\bfollow up\b", r"\btake the lead\b", r"\bown\b",
    r"\bETA\b", r"\bdue\b", r"\bby (?:Mon|Tue|Wed|Thu|Fri|Sat|Sun|\d{1,2}/\d{1,2}|\w+ \d{1,2})\b",
]

_due_regex = re.compile(r"\bby ([A-Za-z]{3,9} \d{1,2}|\d{1,2}/\d{1,2}|\w+day|\bMonday|\bTuesday|\bWednesday|\bThursday|\bFriday)\b",
                        re.IGNORECASE)

_leading_fillers = re.compile(
    r"^(?:Okay|So|Alright|Also|Then|Please|Yeah|Yes|No|Right|Great)[\s,:-]*\s*", re.IGNORECASE
)

def _extract_due(text: str):
    m = _due_regex.search(text)
    return m.group(1) if m else None

def _rewrite_to_task(s: str) -> str:
    """Rewrite a sentence into an imperative task."""
    original = s.strip()

    # Strip leading fillers and trailing punctuation
    s = _leading_fillers.sub("", original).strip().rstrip(". ")

    # Normalize common future/requests -> imperative
    replacements = [
        (r"\bI['’]ll\b\s+", ""), (r"\bI will\b\s+", ""),
        (r"\bWe will\b\s+", ""), (r"\bWe need to\b\s+", ""),
        (r"^\s*Need to\s+", ""), (r"^\s*Please\s+", ""),
        (r"\bwill\b\s+", ""), (r"\s*,?\s*please$", ""),
    ]
    for pat, rep in replacements:
        s = re.sub(pat, rep, s, flags=re.IGNORECASE).strip()

    # Common “I will X” forms that leave pronouns behind
    s = re.sub(r"^(?:I|We)\s+(?=[a-z])", "", s, flags=re.IGNORECASE).strip()

    # Normalize “follow up with/on …” to “Follow up with/on …”
    s = re.sub(r"^(follow up\b)", lambda m: m.group(1).capitalize(), s, flags=re.IGNORECASE)

    # Capitalize first verb/word
    if s:
        s = s[0].upper() + s[1:]

    return s or original

def extract_action_items(transcript: str) -> List[Dict[str, Any]]:
    """Rule-based extractor + rewrite to imperative task."""
    nlp = get_nlp()
    items: List[Dict[str, Any]] = []

    for speaker, content in split_by_speaker(transcript):
        doc = nlp(content)
        for sent in doc.sents:
            s = sent.text.strip()
            if any(re.search(pat, s, flags=re.IGNORECASE) for pat in ACTION_PATTERNS):
                due = _extract_due(s)
                task = _rewrite_to_task(s)
                items.append({
                    "speaker": speaker,
                    "item": s,   # raw sentence (kept for debugging/reference)
                    "task": task,  # ← reworded, imperative task
                    "due": due
                })
    return items
