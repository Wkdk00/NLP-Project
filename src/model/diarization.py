from pyannote.audio import Pipeline


def load_diarization_model(hf_token):
    print("🔄 Загрузка модели диаризации...")
    try:
        pipeline = Pipeline.from_pretrained(
            "pyannote/speaker-diarization-3.1",
            use_auth_token=hf_token
        )
        # Критические параметры:
        pipeline.instantiate({
            "clustering": {
                "method": "average",
                "threshold": 0.7,
                "min_cluster_size": 3
            },
            "segmentation": {
                "min_duration_off": 0.5
            }
        })
        return pipeline
    except Exception as e:
        print(f"❌ Ошибка загрузки модели диаризации: {str(e)}")
        return None

def find_speaker(diarization, start_time, end_time):
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        if turn.start <= start_time <= turn.end or turn.start <= end_time <= turn.end:
            return speaker
    return "UNKNOWN"
