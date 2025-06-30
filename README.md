# mistral.gguf
# Building an Offline AI Chatbot with "Mistral 7B + Gradio + CSV Logging" 

💡 What This Project Does:
 ✅ Runs an LLM locally using llama-cpp with a .gguf version of Mistral-7B
 ✅ Handles real-time question-answering with natural language prompts
 ✅ Records all conversation history (user + assistant messages) into a structured CSV file
 ✅ Uses Gradio for a lightweight, user-friendly chat UI
 ✅ 100% offline — no OpenAI or IBM billing or dependency!
 
 🔧Tech Stack:
🧠 Model: mistral-7b-instruct-v0.1.Q4_0.gguf
🐍 Python libraries: llama-cpp-python, gradio, csv, os
📂 Chat Log: Appends to chat_history.csv after every interaction
🎛️ Interface: Built using Gradio with custom input/output text boxes

🧠 Why I Did This:
With increasing interest in privacy-first AI and offline solutions, I wanted to explore how language models can be embedded locally for use cases like:
Chat assistants for enterprises without internet access
Private research tools
Lightweight AI interfaces for teaching and demos
Prototypes without vendor lock-in or cost barriers
Imagine being able to use an AI model like ChatGPT...
 ⚡ without internet
 ⚡ without API costs
 ⚡ with full control over the model
