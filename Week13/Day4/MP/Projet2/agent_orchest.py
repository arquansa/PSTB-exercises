import requests
import json
import os
from dotenv import load_dotenv
import ollama  # ou Groq/OpenAI
import ast
from urllib.parse import quote
import sys

load_dotenv()
LLM_BACKEND = os.getenv("LLM_BACKEND", "ollama")
MCP_SERVERS = json.load(open("servers_config.json"))
#print("Serveurs MCP configurés :")
#for s in MCP_SERVERS:
#    print(" -", s)
def get_available_tools():
    tools = []
    for server in MCP_SERVERS:
        try:
            print(f"\n[INFO] Interrogation de {server}/metadata")
            response = requests.get(f"{server}/metadata")
            response.raise_for_status()
            meta = response.json()
            print(f"[DEBUG] Réponse reçue depuis {server}: {meta}")

            if "tools" in meta:
                for tool in meta["tools"]:
                    tools.append({
                        "name": tool["name"],
                        "description": tool["description"],
                        "endpoint": f"{server}/infer/{quote(tool['name'])}"
                        #"endpoint": f"{server}/infer/{tool['name']}"
                    })
            elif "name" in meta and "description" in meta:
                tools.append({
                    "name": meta["name"],
                    "description": meta["description"],
                    #"endpoint": f"{server}/infer/{meta['name']}"
                    "endpoint": f"{server}/infer/{quote(tool['name'])}"
                })
            else:
                print(f"[AVERTISSEMENT] Format de metadata inconnu pour {server}: {meta}")

        except Exception as e:
            print(f"[ERREUR] Problème avec {server} – {e}")
    return tools


def ask_llm_for_plan(prompt, tools):
    #print(tools) #Affiche les outils disponibles
    tools_str = "\n".join([f"- {t['name']}: {t['description']}" for t in tools])
    system_prompt = f"""Planifie les appels MCP nécessaires pour répondre à une consigne utilisateur.

Compose plusieurs outils dans le bon ordre.

Tu DOIS répondre UNIQUEMENT par une liste Python, par ex: ["outil1", "outil2"]

Architecture du projet agent intelligent. Tu peux utiliser ces outils :
{tools_str}

Choisis ceux à utiliser (et dans quel ordre) pour accomplir la tâche suivante :
'{prompt}'

RÉPONDS STRICTEMENT PAR UNE LISTE PYTHON, SANS TEXTE SUPPLÉMENTAIRE.
"""

    res = ollama.chat(model="llama3", messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ])
    try:
         plan = ast.literal_eval(res['message']['content'])
         if not isinstance(plan, list):
            raise ValueError("Le plan n'est pas une liste.")
         return plan
    except Exception as e:
        print(f"Erreur lors de l'analyse du plan généré : {e}")
        print("Contenu brut retourné par le LLM :", res['message']['content'])
    return []

def execute_plan(plan, user_input, tools):
    result = user_input
    for step in plan:
        tool = next(t for t in tools if t["name"] == step)
        try:
            response = requests.post(tool["endpoint"], json={"input": result})
            print(f"[DEBUG] Réponse de {step} : {response.text}")
            result = response.json().get("output")
        except Exception as e:
            return f"[Erreur à l'étape {step}] : {e}"
    
    return result

def run_pipeline():
    if sys.stdin.isatty(): 
        prompt = input("Entrez votre consigne : ") 
    else: 
        prompt = sys.stdin.read().strip()

    try:
        tools = get_available_tools()
    except Exception as e:
        print(f"Erreur lors de la récupération des outils : {e}")
        return

    if not tools:
        print("❌ Aucun outil disponible. Vérifie tes serveurs MCP.")
        return
    
    print("Outils détectés 2.0 :")
    for t in tools:
        print(f" - {t['name']}: {t['description']}")

    plan = ask_llm_for_plan(prompt, tools)
    print(f"Plan proposé : {plan}")
    result = execute_plan(plan, prompt, tools)
    print("\nRésultat final :\n", result)

if __name__ == "__main__":
    run_pipeline()