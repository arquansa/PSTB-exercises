Fichier README.md du projet Agent MCP + Streamlit, incluant :
* Description du projet
* Instructions d'installation
* Utilisation (CLI et Streamlit)
* Configuration via .env et .env.example
* Stack technique utilisée
* Structure des fichiers

# Mini-Projet : Agent MCP + Résumeur LLM

Ce projet est une démonstration d'un **agent intelligent orchestrant un serveur MCP** (compatible avec FastAPI) pour résumer un texte. Il inclut :

- Un serveur MCP (`summarizer_server.py`)
- Un agent qui appelle ce serveur (`agent.py`)
- Une interface utilisateur Streamlit (`app.py`)

---

##  Objectifs

- Comprendre le protocole MCP (Machine Control Protocol)
- Construire un serveur d'outil (résumeur) avec FastAPI
- Créer un agent LLM orchestrateur (via Ollama)
- Intégrer le tout dans une interface utilisateur simple (CLI et Streamlit)

---

##  Prérequis

- Python 3.10+ installé
- [Ollama](https://ollama.com/) installé (ou une API Groq/OpenAI)
- `git`, `pip` et un terminal
- (Optionnel) Environnement virtuel (`python -m venv .venv`)

---

##  Installation

```bash
git clone https://github.com/ton-utilisateur/ton-projet.git
cd ton-projet

# Créer et activer un environnement virtuel
python -m venv .venv
.\.venv\Scripts\activate    # Windows
# source .venv/bin/activate  # Mac/Linux

# Installer les dépendances
pip install -r requirements.txt

# Copier le fichier de configuration
cp .env.example .env

Lancer l'application
1. Lancer le serveur MCP
python -m uvicorn summarizer_server:app --reload --port 5000
Accès santé : http://localhost:5000/healthz

2. Utiliser l'agent via le terminal (CLI)
python agent.py

3. Lancer l'interface Streamlit
streamlit run app.py

Configuration .env
Le fichier .env permet de définir les paramètres du projet.
Exemple dans .env.example :
CUSTOM_SERVER_URL=http://localhost:5000
LLM_BACKEND=ollama
OLLAMA_MODEL=llama3
# GROQ_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx

Structure du projet
.
??? app.py                  # Interface utilisateur Streamlit
??? agent.py                # Agent LLM qui appelle le serveur MCP
??? summarizer_server.py    # Serveur FastAPI compatible MCP
??? .env.example            # Exemple de configuration
??? requirements.txt        # Dépendances Python
??? README.md               # Documentation du projet

Stack technique
* Langage : Python 3.10+
* LLM : Ollama (LLaMA 3 / Mistral) ou GroqCloud
* Serveur API : FastAPI + Uvicorn
* Orchestration : Appels directs via requests
* Interface : Streamlit (ou CLI)

Fonctionnalités livrées
* Un serveur MCP /infer, /healthz, /metadata
* Un agent LLM fonctionnel
* Une UI (CLI + Streamlit)
* Projet reproductible avec .env et requirements.txt



