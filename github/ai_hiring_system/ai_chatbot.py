from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Free AI model from Hugging Face (change model if needed)
chatbot = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")

@app.get("/")
def home():
    return {"message": "AI Chatbot for Hiring System is running!"}

@app.get("/chat")
def chat(query: str):
    response = chatbot(query, max_length=100, do_sample=True)
    return {"reply": response[0]["generated_text"]}
