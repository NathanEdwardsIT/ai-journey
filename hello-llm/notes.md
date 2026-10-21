# Initial Script Run:

import ollama

response = ollama.chat(

model = "llama3.1:8b",
messages = [{"role": "user", "content": "Explain what a ML token is in two sentences."}],)

print(response["message"]["content"])

# Initial Response:

A ML token, short for Merkle Leaf token, is a type of digital token that represents a specific amount of value stored on a decentralized finance (DeFi) platform, such as Compound or Aave. It's essentially a digital receipt or a proof of deposit that demonstrates the user's ownership of a certain amount of cryptocurrency, such as USDC or DAI, which can be used as collateral to borrow other assets.

# Notes

Prompt was too vague for proper response. A clearer request would provide an answer in greater detail and accuracy (See "llm-prompt-engineering"). 

# Updated Prompt & Response:

"Explain what a machine learning token is and what tokenization is. Explain it simply and accurately."

Response: **Why is Tokenization Important?**

Tokenization is a crucial step in natural language processing (NLP) and machine learning, as it allows models to:

1. Understand the meaning of text
2. Identify patterns and relationships between words and phrases
3. Analyze and classify text into different categories

By breaking down text into individual tokens, machine learning models can gain a deeper understanding of language and make more accurate predictions.

# Interesting Prompt Change

I used a new prompt and received detailed information: "Explain to me what the llama3.1:8b model is, it's effectiveness, the naming convention, etc."

# Response:

You're referring to the llama (Large Language Model Meta AI) model!

**What is LLaMA?**

LLaMA is a large language model developed by Meta AI, the research and development arm of Meta Platforms, Inc. It's a transformer-based model, similar to other popular language models like BERT, RoBERTa, and others.

**Model Variants:**

The naming convention for LLaMA models follows a specific format: `llama<version>:<size>`. Here's a breakdown of the naming components:

* `llama`: The prefix indicating that it's a LLaMA model.
* `<version>`: A numerical version number, which represents the model's architecture and training data. For example, `3.1` indicates that it's the 3rd major version of the model, with a specific architecture and training data.
* `<size>`: A size suffix, which represents the number of parameters or the model's capacity. In this case, `8b` indicates that the model has approximately 8 billion parameters.

# Prompt Failure

When I changed the prompt to say "Do this in one paragraph", the prompt failed:

"There is no information on a "llama3.1:8b model". It's possible that you may be thinking of a different model, such as the BERT (Bidirectional Encoder Representations from Transformers) model, which is a pre-trained language model developed by Google. BERT has undergone various updates and fine-tunings, including BERT-base (12-layer), BERT-large (24-layer), and others, but I couldn't find any information on a "llama3.1:8b model". If you could provide more context or clarify what you're referring to, I'd be happy to help."

# Options = {"num_predict": 20}

Produced a response that was cut off at at a 20-token response. Similar idea to a max-tokens idea in a paid API.

# Print(response["prompt_eval_count])
# Print (response["eval_count"])

prompt_eval_count produced the amount of tokens required for the prompt, whereas eval_count produced the amount of tokens needed to produce the response.

# What is the "temperature" parameter?

Originally ran the prompt with no temperature parameter, producing the same response. After adding a temperature of 1.0, each response had differing amounts of quality, context, and token count. Essentially, the temperature of a prompt gives the model insight into the degree of creativity & randomness that the response should have.

# Tokens Per Second Notes

I just learned that ollama models report the duration of a prompt's evaluation in nanoseconds. This means that in order to get the amount of tokens per second, we have to divide the eval_duration by 1e9 (1 x 10^9) in order to get it mathematically correct.

I originally started this project running llama3.1:8b, which has a context window of 4096. Running this model on my GPU, an RTX 5060Ti, produces an average tokens/second of 77.569. 

The next model that I decided to run was from the same family (qwen3:8b), with a slightly larger VRAM requirement of roughly 6GB. This is still a far-cry from the 16GB VRAM limitations of the GPU, meaning it should run relatively smoothly.

The qwen3:8b model is trained off slightly more tha double the amount of tokens (36 trillion). However, it has a context window of 32k compared to 128k tokens that llama3.1:8b has.

The qwen3:8b model produced a smaller tokens/second, standing at roughly 66 tokens/s. 

# Tiktokenizer Notes

After a couple minutes of experimentation, I found it surprising that the same word typed in the same format repeatedly would sometimes be broken down into different tokens.

Some research that I did showed that common words are oftentimes algorithmically broken down into a single token, while more complex or uncommon words can be broken down into pairs, or pieces of tokens. For example, a word like tokenization may get broken down into "token" + "ization". 

# Chatbot.py Notes

The simple chatbot that I created has one key thing to note: It reads the entire conversation history every time it goes to produce a reply. This is because at the top there is an empty list called "history", that appends user input & model response into it. 

What this means is that the model itself has no memory. The "memory" it has is because each and every message + response is added to a list that it then reads from before responding.

# How I Broke the Chatbot

Firstly, I went ahead and deleted the following line:

history.append({"role": "assistant", "content": answer})

This is the line that appends the chatbot's response to the "history" list. When this line is removed, it means that the chatbot can only ever see my previous inputs, and not the responses it has given. This means it will consistently answer the same questions again as it does not know it already answered it.

Then, I went ahead and deleted this line:

history.append({"role": "user", "content": user_text})

Which breaks things in a different way. What this does is completely removes the feature that appends my input to the history list. This breaks the model because this line comes before it goes to read my input in order to formulate a reply. With no question/input, it has nothing to answer and thus breaks.