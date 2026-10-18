import ollama

response = ollama.chat(

model = "llama3.1:8b",
messages = [{"role": "user", "content":"You are an AI educator explaining technical concepts to beginners. Use the following example to understand the desired teaching style, structure, and level of detail. Example Question: What is an embedding in machine learning? Example Answer: An embedding is a way of representing information as a collection of numbers. These numbers help machine learning models identify similarities and relationships between pieces of information. For example, the words 'cat' and 'dog' might have similar numerical representations because they share characteristics, while 'cat' and 'airplane' would generally be less similar. Embeddings matter because computers operate on numbers, and these representations allow models to work with the meaning and relationships of text, images, and other data. Now answer the following question using the same style: What is a token in the context of large language models? Requirements: Begin with a clear, simple definition. Explain the concept using a concrete example. Describe why it matters in practice. Use accessible language. Keep your response under 200 words."}])
print(response["message"]["content"])

