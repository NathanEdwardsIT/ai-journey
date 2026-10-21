import ollama
MODEL = "llama3.1:8b"
history = []

while True:
    user_text = input("You: ")
    if user_text == "quit":
        break
    history.append({"role": "user", "content": user_text})
    reply = ollama.chat(model=MODEL, messages=history)
    answer = reply["message"]["content"]
    history.append({"role": "assistant", "content": answer})
    print("Model: ", answer)
