import requests
import os
import json
import ollama  # ou openai/groq si souhaité

MCP_SERVER_URL = os.getenv("CUSTOM_SERVER_URL", "http://localhost:5000")


def ask_llm(prompt):
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

def call_mcp_tool(user_input):
    # Envoie au serveur MCP
    response = requests.post(f"{MCP_SERVER_URL}/infer/summarizer", json={"input": user_input})
    return response.json().get("output")

def run_pipeline():
    user_query = input("👤 Entrez votre texte à résumer : ")

    print("📤 Envoi au serveur de résumé...")
    mcp_result = call_mcp_tool(user_query)

    print("🤖 Résumé généré :")
    print(mcp_result)

if __name__ == "__main__":
    run_pipeline()