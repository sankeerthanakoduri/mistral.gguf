from llama_cpp import Llama
import gradio as gr

# Load local model
llm = Llama(model_path="C:/llama_models/mistral.gguf")

def generate_response(prompt):
    output = llm(prompt, max_tokens=256, temperature=0.7)
    return output["choices"][0]["text"]

iface = gr.Interface(
    fn=generate_response,
    inputs="text",
    outputs="text",
    title="Local Mistral Chatbot",
    description="Chatbot running offline, no API key needed"
)

iface.launch()
