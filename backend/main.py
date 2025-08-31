from fastapi import FastAPI
import requests
import os

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bienvenido a tu app con LLM + Docker + Ollama"}

@app.post("/preguntar")
def preguntar(pregunta: str):
    data = {
        "model": "gpt-oss:20b",  # Cambia si usas otro modelo
        "prompt": pregunta,
        "stream": False
    }
    try:
        response = requests.post(f"{OLLAMA_HOST}/api/generate", json=data)
        return {"respuesta": response.json()["response"]}
    except Exception as e:
        return {"error": str(e)}
