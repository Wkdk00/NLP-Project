from typing import List, Dict
from src.model.diarization import find_speaker


def match_speakers_to_segments(transcript_segments: List[Dict], diarization_result) -> List[Dict]:
    matched_segments = []
    for segment in transcript_segments:
        speaker = find_speaker(diarization_result, segment['start'], segment['end'])
        matched_segments.append({
            'start': segment['start'],
            'end': segment['end'],
            'speaker': speaker,
            'text': segment['text']
        })
    return matched_segments
