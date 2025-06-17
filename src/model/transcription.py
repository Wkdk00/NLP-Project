import whisper

"""Загрузка модели транскрибации"""

def load_transcription_model(model_size="base"):
    print("🔄 Загрузка модели транскрибации...")
    try:
        return whisper.load_model(model_size)
    except Exception as e:
        print(f"❌ Ошибка загрузки модели транскрибации: {str(e)}")
        return None