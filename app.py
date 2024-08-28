import os
import gradio as gr

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me a funny joke",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)

def chat_with_groq(sender_name, receiver_name, about_receiver, project_name, project_details, key_benefits, additional_info=None):

    full_message = (
        f"Compose a personalized email to {receiver_name}, starting with a friendly greeting which include details about the receiver from {about_receiver}. Briefly introduce yourself {sender_name} and express your enthusiasm for sharing details about {project_name}. Describe the {project_details} in a way that highlights its innovative aspects and its potential impact on {receiver_name} or their business. Clearly outline the {key_benefits} of the project, emphasizing how it can address specific challenges or goals that {receiver_name} might have. End the email by inviting {sender_name} to discuss the project further, and provide your contact information shivam10lam@gmail.com for follow-up."
        
)

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": full_message,
        }
    ],
    model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content


#add UI
iface = gr.Interface(
    fn=chat_with_groq,
    inputs=[
        gr.Textbox(label="Sender Name"),
        gr.Textbox(label="Receiver Name"),
        gr.Textbox(label="About Receiver"),
        gr.Textbox(label="Project Name"),
        gr.Textbox(label="Project Details"),
        gr.Textbox(label="Key Benefits")
        
    ],
    outputs=gr.Textbox(label="Chatbot Response"),
    title="Personalized Email Generator ChatBot",
    description="Send a personalized email using Groq-powered chatbot"
)

if __name__=="__main__":
    iface.launch()