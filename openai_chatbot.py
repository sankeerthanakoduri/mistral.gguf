import openai
import gradio as gr

# Set your OpenAI key
openai.api_key = "<YOUR_API_KEY>"  # Replace with your key

# Function to get GPT response
def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Or "gpt-3.5-turbo" if you want a cheaper option
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ Error: {e}"

# Gradio interface
chat_ui = gr.Interface(
    fn=chat_with_gpt,
    inputs=gr.Textbox(label="Ask something", lines=2, placeholder="What's AI?"),
    outputs=gr.Textbox(label="GPT Response"),
    title="OpenAI GPT Chatbot",
    description="Ask any question and get a GPT-powered response!"
)

# Launch the app
chat_ui.launch()
