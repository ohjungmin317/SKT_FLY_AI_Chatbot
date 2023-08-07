# ChatGPT API 이용한 나만의 심리 상담 챗봇 만들기

import gradio as gr # gradio 사용하여 챗봇 ui 사용
import random
import time

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    def respond(message, chat_history):
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"]) # 해당 챗봇에서 3개가 랜덤 값으로 나오게 된다.
        chat_history.append((message, bot_message))
        time.sleep(1)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch() # main에서 launch() 시행 