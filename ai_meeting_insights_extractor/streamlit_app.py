import streamlit as st
from typing import List
from app.preprocess import normalize, chunk_text
from app.model import summarize_chunks, get_generator
from app.extract import extract_action_items
import pandas as pd

st.set_page_config(page_title="AI Meeting Insights Extractor", layout="wide")

st.title("AI Meeting Insights Extractor")
st.caption("Upload a transcript (.txt) to generate a summary, extract action items, and ask questions.")

with st.sidebar:
    st.header("Settings")
    model_name = st.selectbox(
        "Model",
        options=[
            "facebook/bart-large-cnn",  # recommended
            "google/flan-t5-base",
            "google/flan-t5-large",
            "google/flan-t5-small",
        ],
        index=0,
    )
    bullets = st.slider("Summary bullets", 3, 10, 5)
    max_chunk_chars = st.number_input("Max chunk chars", 1000, 8000, 2000, step=500)
    st.markdown("---")
    st.write("Tip: Try BART first; use *small* T5 only on very low-resource machines.")

tab1, tab2, tab3 = st.tabs(["📄 Upload", "📝 Summary & Actions", "❓ Q&A"])

with tab1:
    st.subheader("Upload transcript (.txt) or paste text")
    uploaded = st.file_uploader("Choose a .txt file", type=["txt"])
    text_input = st.text_area("...or paste transcript here", height=200, placeholder="Speaker: text...")
    col_a, col_b = st.columns(2)
    with col_a:
        run_btn = st.button("Run Insights")
    with col_b:
        clear_btn = st.button("Clear")

    if clear_btn:
        st.session_state.clear()

    if run_btn:
        transcript = uploaded.read().decode("utf-8", errors="ignore") if uploaded else text_input

        if not transcript.strip():
            st.warning("Please upload or paste a transcript.")
        else:
            # 1) For summarization: lighter normalization (can collapse newlines)
            text_for_summary = normalize(transcript, keep_newlines=False)
            chunks = chunk_text(text_for_summary, max_chars=int(max_chunk_chars))

            with st.status("Loading model and generating summary...", expanded=False):
                summary = summarize_chunks(chunks, bullets=bullets, model_name=model_name)

            # 2) For action items: preserve newlines so speaker parsing works
            text_for_actions = normalize(transcript, keep_newlines=True)
            with st.status("Extracting action items...", expanded=False):
                actions = extract_action_items(text_for_actions)

            # Save for other tabs
            st.session_state["summary"] = summary
            st.session_state["actions"] = actions
            # Use preserved-newlines transcript for Q&A grounding
            st.session_state["transcript"] = text_for_actions
            st.success("Done! Check the next tab.")

with tab2:
    st.subheader("Summary")
    if "summary" in st.session_state:
        for i, b in enumerate(st.session_state["summary"], 1):
            st.markdown(f"- {b}")
    else:
        st.info("Run insights first.")

    st.subheader("Action Items")
    if "actions" in st.session_state:
        actions = st.session_state["actions"]
        if actions:
            # Prefer the reworded 'task' (falls back to raw 'item' if needed)
            display_actions = []
            for a in actions:
                display_actions.append({
                    "owner": a.get("speaker"),
                    "task": a.get("task") or a.get("item"),
                    "due": a.get("due"),
                })
            df = pd.DataFrame(display_actions)
            st.dataframe(df, use_container_width=True)

           
        else:
            st.write("No action items detected.")
    else:
        st.info("Run insights first.")

with tab3:
    st.subheader("Ask a question about this meeting")
    q = st.text_input("Your question", placeholder="What did the CFO commit to?")
    ask = st.button("Ask")
    if ask:
        if "transcript" not in st.session_state:
            st.warning("Please run insights first (or upload a transcript).")
        elif not q.strip():
            st.warning("Type a question.")
        else:
            gen = get_generator(model_name)
            prompt = (
                "Answer the question using ONLY the transcript below. "
                "If the answer is not present, say 'Not stated.'\n\n"
                f"Transcript:\n{st.session_state['transcript']}\n\n"
                f"Question: {q}\nAnswer:"
            )
            with st.status("Thinking...", expanded=False):
                out = gen(prompt, max_new_tokens=180, num_beams=4)[0]["generated_text"]
            st.markdown(f"**Answer:** {out}")
