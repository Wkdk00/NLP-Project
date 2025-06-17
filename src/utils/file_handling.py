import os
from typing import List, Dict


def check_file_exists(file_path: str) -> bool:
    """Проверка существования файла"""
    if not os.path.exists(file_path):
        print(f"❌ Файл {file_path} не найден!")
        return False
    return True


def save_results(segments: List[Dict], output_path: str) -> None:
    """Сохранение результатов в файл"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        for segment in segments:
            line = f"[{segment['start']:.1f}-{segment['end']:.1f}] {segment['speaker']}: {segment['text']}\n"
            f.write(line)

    print(f"✅ Результат сохранён в {output_path}")
    print(f"🔢 Статистика: {len(segments)} сегментов, {len(set(s['speaker'] for s in segments))} спикеров")