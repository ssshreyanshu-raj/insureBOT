import streamlit as st
import tempfile
import os
from transcriber import transcribe_audio
from extractor import extract_data
from translator import translate_lines
from intent_predictor import predict_intents

st.set_page_config(page_title="InsureBot", layout="centered")
st.title("InsureBot – Hindi Call Analyzer")

uploaded = st.file_uploader("Upload a .wav file", type=["wav"])

if uploaded:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded.read())
        audio_path = tmp.name

    if st.button("Run Analysis"):
        with st.spinner("Analyzing call..."):
            lines = transcribe_audio(audio_path)
            data = extract_data(lines)
            translated = translate_lines(lines)
            intents = predict_intents(translated)

        st.success("✅ Analysis complete!")

        st.subheader("📝 Hindi Transcription")
        st.write("\n".join(lines))

        st.subheader("📦 Extracted Policy Info")
        st.json(data)

        st.subheader("🌐 English Translations")
        st.write("\n".join(translated))

        st.subheader("🤖 Predicted Intents")
        for i, intent in enumerate(intents):
            st.write(f"Line {i+1}: {intent}")

        os.remove(audio_path)
