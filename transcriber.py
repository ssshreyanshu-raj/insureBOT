from faster_whisper import WhisperModel

def transcribe_audio(audio_path):
    model = WhisperModel("large-v2", compute_type="int8")
    segments, _ = model.transcribe(audio_path)
    return [seg.text for seg in segments]
