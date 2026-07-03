import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def run_llm(prompt: str):
    payload = {
        "model": "phi3:latest",
        "prompt": prompt,
        "stream": False
    }

    try:
        r = requests.post(OLLAMA_URL, json=payload)
        r.raise_for_status()
        return r.json().get("response", "No response").strip()
    except Exception as e:
        return f"Error: {str(e)}"