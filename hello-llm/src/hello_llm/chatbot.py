import ollama
import json
from pathlib import Path
HERE = Path(__file__).parent
CHAT_PATH = HERE / 'system.json'
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
    history.append({"role": "assistant", "content": answer})
    print("Model: ", answer, history)