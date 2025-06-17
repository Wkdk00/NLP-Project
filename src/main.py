import os
import warnings

from model.diarization import load_diarization_model
from model.transcription import load_transcription_model
from model.deepseek import load_deepseek
from utils.file_handling import check_file_exists, save_results
from utils.speachbox import match_speakers_to_segments

from config import CONFIG

# Отключаем предупреждения
warnings.filterwarnings("ignore")


def process_audio(file_path: str, hf_token: str):
    """Основной процесс обработки аудио"""
    if not check_file_exists(file_path):
        return

    # 1. Загрузка моделей
    print("🔄 Загрузка моделей...")
    diarization_model = load_diarization_model(hf_token)
    whisper_model = load_transcription_model()

    if not diarization_model or not whisper_model:
        print("❌ Ошибка загрузки моделей")
        return

    try:
        # 2. Диаризация
        print("🔊 Анализ спикеров...")
        diarization = diarization_model(file_path)

        # 3. Транскрибация
        print("✍️ Транскрибация аудио...")
        transcript = whisper_model.transcribe(file_path, language=CONFIG["language"])

        # 4. Сопоставление спикеров с текстом
        print("🧩 Сопоставление данных...")
        matched_segments = match_speakers_to_segments(transcript["segments"], diarization)

        # 5. Сохранение сырых результатов
        raw_output_path = os.path.join(CONFIG["output_dir"], "raw_transcript.txt")
        save_results(matched_segments, raw_output_path)

        # 6. Оценка продавца
        print("🧠 Анализ данных...")
        result = load_deepseek()
        print("🔥 Оценка продавца...")
        print(result)

    except Exception:
        print(f"❌ Ошибка обработки: {str(Exception)}")
        if hasattr(Exception, 'response'):
            print(f"Детали: {Exception.response.text}")



if __name__ == "__main__":
    os.makedirs(CONFIG["output_dir"], exist_ok=True)
    process_audio(CONFIG["audio_file"], CONFIG["hf_token"])