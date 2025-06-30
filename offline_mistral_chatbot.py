import csv
import os
from llama_cpp import Llama
import gradio as gr

# ✅ Path to your GGUF model (update if needed)
model_path = r"C:\Users\Admin\Downloads\mistral-7b-instruct-v0.1.Q4_0.gguf"

# ✅ Initialize Llama model
llm = Llama(model_path=model_path, n_ctx=2048)

# ✅ Chat history and CSV setup
chat_history = []
csv_file_path = "chat_history.csv"

# ✅ Create CSV with headers if it doesn't exist
if not os.path.exists(csv_file_path):
    with open(csv_file_path, mode="w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["User Input", "Assistant Response"])

# ✅ Function to generate response and log chat
def generate_response(prompt_txt):
    chat_history.append({"role": "user", "content": prompt_txt})

    # Build conversation prompt
    full_prompt = ""
    for msg in chat_history:
        role = msg["role"]
        content = msg["content"]
        full_prompt += f"{'User' if role == 'user' else 'Assistant'}: {content}\n"
    full_prompt += "Assistant:"

    # Get response
    response = llm(full_prompt, max_tokens=512, stop=["User:", "Assistant:"])
    reply = response["choices"][0]["text"].strip()

    # Update history and write to CSV
    chat_history.append({"role": "assistant", "content": reply})
    with open(csv_file_path, mode="a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([prompt_txt, reply])

    return reply

# ✅ Gradio Chat UI
gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(label="Your Question"),
    outputs=gr.Textbox(label="Assistant Response"),
    title="Local Mistral Chatbot (Offline)",
    description="Chat offline using Mistral 7B Instruct. No API or internet needed."
).launch()
