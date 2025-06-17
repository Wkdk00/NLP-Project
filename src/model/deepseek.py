import requests
from src.config import CONFIG
import os

def load_deepseek():
    url = "https://api.intelligence.io.solutions/api/v1/chat/completions"

    # Исправленный путь к файлу
    file_path = os.path.join("output", "raw_transcript.txt")

    with open(file_path, "r", encoding="utf-8") as file:
        user_content = file.read()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CONFIG['deepseek_token']}"
    }

    data = {
        "model": "deepseek-ai/DeepSeek-R1",
        "messages": [
            {
                "role": "system",
                "content": "оцени вежливость продавца от 1 до 10 (Оценивай более лояльнее если продавец не грубит, здоровается и прощается, то это 10 баллов) ты должен написать только цифру и не писать других слов, не давать вообще никаких комментариев"
            },
            {
                "role": "user",
                "content": user_content
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    data = response.json()
    text = data['choices'][0]['message']['content']
    return text.split('</think>\n\n')[1]

#res = load_deepseek()
#print(res)