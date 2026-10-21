import ollama
import json
from pathlib import Path
HERE = Path(__file__).parent
CHAT_PATH = HERE / 'system.json'
LOG_PATH = HERE / 'log.json'
MODEL = "llama3.1:8b"

if CHAT_PATH.exists() and CHAT_PATH.stat().st_size > 0:

    with open(CHAT_PATH, 'r') as file:
        history = json.load(file)
else:
    history = []
    
while True:
    user_text = input("You: ")
    if user_text == "quit":
        with open('C:/Users/natnat/OneDrive/Documents/ML Learning/hello-llm/src/hello_llm/system.json', 'w') as file:
            json.dump(history, file, indent=2)
        break
    history.append({"role": "user", "content": user_text})
    reply = ollama.chat(model=MODEL, messages=history)
    answer = reply["message"]["content"]
    tokens_per_second = reply["eval_count"] / (reply["eval_duration"] / 1e9)
    tokens_per_second_string = f"Tokens/s: {tokens_per_second:.1f}"
    history.append({"role": "assistant", "content": answer})
    history.append({"role": "system", "content": tokens_per_second_string})
    print("Model: ", answer)