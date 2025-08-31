import re
from typing import List, Dict, Any
from .preprocess import get_nlp, split_by_speaker

ACTION_PATTERNS = [
    r"\bwill\b",
    r"\bneed to\b",
    r"\bplease\b",
    r"\bby (?:Mon|Tue|Wed|Thu|Fri|Sat|Sun|\d{1,2}/\d{1,2}|\w+ \d{1,2})\b",
    r"\bdue\b",
    r"\bfollow up\b",
    r"\bETA\b",
    r"\btake the lead\b",
    r"\bown\b",
]
_due_regex = re.compile(r"\bby ([A-Za-z]{3,9} \d{1,2}|\d{1,2}/\d{1,2}|\w+day)\b", re.IGNORECASE)

def extract_action_items(transcript: str) -> List[Dict[str, Any]]:
    nlp = get_nlp()
    items: List[Dict[str, Any]] = []
    for speaker, content in split_by_speaker(transcript):
        doc = nlp(content)
        for sent in doc.sents:
            s = sent.text.strip()
            if any(re.search(pat, s, flags=re.IGNORECASE) for pat in ACTION_PATTERNS):
                due = None
                m = _due_regex.search(s)
                if m:
                    due = m.group(1)
                cleaned = re.sub(r"^(Okay|So|Alright|Also|Then|Please)\s*,?\s*", "", s, flags=re.IGNORECASE)
                items.append({"speaker": speaker, "item": cleaned, "due": due})
    return items
