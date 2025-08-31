# AI Meeting Insights Extractor

This project provides both an **API** (FastAPI) and a **Streamlit UI** for extracting insights from meeting transcripts.  
It can:
- **Summarize** transcripts into concise bullet points using Hugging Face's Flan-T5 models.
- **Extract action items** with speaker attribution and optional deadlines.
- **Answer questions** about the meeting using grounded LLM-based Q&A.


---

## Quickstart

### 1. Setup Environment
```bash
python -m venv meeting_assistant
source meeting_assistant/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm

2. Run FastAPI
uvicorn app.main:app --reload


API docs: http://127.0.0.1:8000/docs

Example Request
curl -X POST "http://127.0.0.1:8000/insights" \
  -H "Content-Type: application/json" \
  -d @data/sample_transcripts/sample1.json

3. Run Streamlit UI
streamlit run streamlit_app.py


Features:

Upload a transcript .txt or paste text.

Get a summary and action items.

Ask questions about the transcript.

Try with:

data/sample_transcripts/sample_uploadable.txt

⚙️ Settings

Model: choose between flan-t5-small (fast), flan-t5-base (balanced), flan-t5-large (more accurate).

Summary bullets: adjustable (default: 5).

Max chunk size: controls how transcripts are split before summarization.

🐳 Docker

Build and run in Docker:

docker build -t meeting-insights .
docker run -p 8000:8000 meeting-insights




# AI Meeting Insights Extractor

## 🧩 Zoom/Teams Compatibility

You can use transcripts exported from **Zoom** or **Microsoft Teams**.

### Supported Formats
- `.txt` — drop in directly (recommended)
