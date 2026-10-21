import ollama

response = ollama.chat(

model = "qwen3:8b",
messages = [{"role": "system", "content": "Explain to me what the llama3.1:8b model is, it's effectiveness, the naming convention, etc. Do this in one paragraph."}],
options={"temperature": 1.0},
)

seconds = response["eval_duration"] / 1e9
tokens_per_second = response["eval_count"] / seconds
print(response["message"]["content"])
print(response["eval_count"])
print(tokens_per_second)