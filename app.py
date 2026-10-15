import os
import traceback
from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv
import gradio as gr

load_dotenv(override=True)

MODEL_NAME = os.getenv("OLLAMA_MODEL")

client = OpenAI(
    base_url=os.getenv("OLLAMA_BASE_URL", ""),
    api_key=os.getenv("OLLAMA_API_KEY"),
)

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def clean(history):
    out = []
    for m in history:
        content = m.get("content", "")
        if isinstance(content, list):
            content = "".join(
                b.get("text", "") if isinstance(b, dict) else str(b) for b in content
            )
        out.append({"role": m["role"], "content": content})
    return out


def chat(message, history):
    try:
        if isinstance(message, dict):
            message = message.get("text", "")
        messages = system + clean(history) + [{"role": "user", "content": message}]

        response = client.chat.completions.create(
            model=MODEL_NAME, messages=messages, tools=tools
        )
        while response.choices[0].finish_reason == "tool_calls":
            msg = response.choices[0].message
            results = handle_tool_calls(msg.tool_calls)
            messages.append(msg)
            messages.extend(results)
            response = client.chat.completions.create(
                model=MODEL_NAME, messages=messages, tools=tools
            )
        return response.choices[0].message.content
    except Exception as e:
        traceback.print_exc()  # el error completo sale en los Logs de Render
        return f"Error técnico: {e}"


if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Digital Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(show_label=False),
    ).launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860)),
        css=CSS,
        js=JS,
        theme=gr.themes.Base(),
    )