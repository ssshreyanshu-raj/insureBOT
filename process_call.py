import sys
from transcriber import transcribe_audio
from extractor import extract_data
from translator import translate_lines
from intent_predictor import predict_intents

if __name__ == "__main__":
    audio_path = sys.argv[1]

    print(f"📞 Processing: {audio_path}")

    # 1. Transcription
    lines = transcribe_audio(audio_path)
    print("📝 Transcription:", lines)

    # 2. Extraction
    data = extract_data(lines)
    print("📦 Extracted Data:", data)

    # 3. Translation
    translated = translate_lines(lines)
    print("🌐 Translated:", translated)

    # 4. Intent Prediction
    intents = predict_intents(translated)
    print("🤖 Intents:", intents)
