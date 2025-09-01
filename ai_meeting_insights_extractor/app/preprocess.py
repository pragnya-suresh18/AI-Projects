import re
from typing import List, Tuple
import spacy

_nlp = None
def get_nlp():
    global _nlp
    if _nlp is None:
        _nlp = spacy.load("en_core_web_sm")
    return _nlp

SPEAKER_LINE = re.compile(r"^\s*([A-Za-z][A-Za-z .'-]{0,40}):\s+(.*)$")
TIMESTAMP = re.compile(r"\[?\(?\d{1,2}:\d{2}(?::\d{2})?\)?\]?")

def clean_line(line: str) -> str:
    line = TIMESTAMP.sub("", line)
    line = re.sub(r"\s+", " ", line).strip()
    return line

def split_by_speaker(text: str) -> List[Tuple[str, str]]:
    items: List[Tuple[str, str]] = []
    current_speaker = "Unknown"
    buffer = []
    for raw in text.splitlines():
        line = clean_line(raw)
        if not line:
            continue
        m = SPEAKER_LINE.match(line)
        if m:
            if buffer:
                items.append((current_speaker, " ".join(buffer).strip()))
                buffer = []
            current_speaker, content = m.group(1).strip(), m.group(2).strip()
            if content:
                buffer.append(content)
        else:
            buffer.append(line)
    if buffer:
        items.append((current_speaker, " ".join(buffer).strip()))
    return items

def normalize(text: str, keep_newlines: bool = True) -> str:
    """
    Standardize whitespace. If keep_newlines=True, keep line breaks so
    split_by_speaker() can detect 'Speaker: ...' per line.
    """
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if keep_newlines:
        lines = []
        for ln in text.splitlines():
            ln = re.sub(r"\s+", " ", ln).strip()
            if ln:
                lines.append(ln)
        return "\n".join(lines).strip()
    else:
        return re.sub(r"\s+", " ", text).strip()

def chunk_text(text: str, max_chars: int = 4000) -> List[str]:
    nlp = get_nlp()
    doc = nlp(text)
    chunks: List[str] = []
    cur = ""
    for sent in doc.sents:
        s = sent.text.strip()
        if len(cur) + len(s) + 1 > max_chars and cur:
            chunks.append(cur.strip())
            cur = s
        else:
            cur = (cur + " " + s).strip()
    if cur:
        chunks.append(cur.strip())
    return chunks
