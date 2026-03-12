# diarization.py
import os
from pyannote.audio import Pipeline

HUGGINGFACE_TOKEN = os.environ.get("HF_TOKEN", "")

_pipeline = None

def _get_pipeline():
    global _pipeline
    if _pipeline is None:
        _pipeline = Pipeline.from_pretrained(
            "pyannote/speaker-diarization-3.1",
            token=HUGGINGFACE_TOKEN
        )
    return _pipeline

def diarize_audio(audio_path):
    pipeline = _get_pipeline()
    diarization = pipeline(audio_path)
    
    # Save RTTM (optional)
    with open("audio.rttm", "w") as rttm:
        diarization.write_rttm(rttm)

    result = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        result.append({
            "speaker": speaker,
            "start": round(turn.start, 2),
            "end": round(turn.end, 2)
        })
    return result
