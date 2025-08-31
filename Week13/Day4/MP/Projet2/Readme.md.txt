# Projet Réseau - Système de Traitement Multi-Agents

Ce projet contient **deux réseaux** indépendants simulant des services backend distincts avec leurs propres environnements, serveurs, orchestrateurs, et interfaces utilisateur.

## Structure du Projet

Projet/
?
??? Projet1/
? ??? .venv-2/ # Environnement virtuel du 1er réseau
? ??? src/
? ? ??? summarizer_server.py # Serveur FastAPI (réseau 1)
? ? ??? agent.py # Orchestrateur (réseau 1)
? ??? app.py # Interface Streamlit (réseau 1) ==> OK fonctionnelle
??? Projet2/
? ??? .venv/ # Environnement virtuel du 2e réseau
? ??? src/
? ? ??? main_server.py # Serveur FastAPI (réseau 2)
? ? ??? agent_orchest.py # Orchestrateur (réseau 2)
? ??? app_2.py # Interface Streamlit (réseau 2) ==>  (non fonctionnelle/facultative)
## ?? Installation des environnements virtuels

### Projet 1 (venv-2)
`
cd Projet1
python -m venv venv-2
venv-2\Scripts\activate  # Windows
pip install -r requirements.txt

## ?? Installation des environnements virtuels

### Projet 1 (venv-2)

cd Projet1
python -m venv venv-2
venv-2\Scripts\activate  # Windows
pip install -r requirements.txt

Lancer les serveurs FastAPI
Projet 1
cd Projet1/src
uvicorn summarizer_server:app --host 0.0.0.0 --port 5000 –reload

Projet 2
cd Projet2/src
uvicorn main_server:app --host 0.0.0.0 --port 8000 --reload

Lancer les orchestrateurs
Projet 1

cd Projet1/src
python agent.py

Projet 2
cd Projet2/src
python agent_orchest.py

Lancer l’interface utilisateur (Streamlit)
Projet 1

cd Projet1
streamlit run app.py (fonctionnelle)

Projet 2
cd Projet2
streamlit run app_2.py (non fonctionnelle)

Outils utiles
Vérification des ports
- Tester si un serveur fonctionne :
curl http://localhost:5000  # ou 8000 selon le projet

- Lister les ports ouverts :
netstat -an | find "LISTEN"

Gestion des dépendances
- Installer les  bibliothèques : pip install -r requirements.txt
-  Mettre à jour requirements.txt : pip freeze > requirements.txt
- Lister les paquets installés :pip list

Notes
- Il est recommandé d’utiliser Visual Studio Code et d’ouvrir deux fenêtres indépendantes (Ctrl+Shift+N) pour isoler les deux environnements.
- Les serveurs doivent être lancés dans la console activée correspondant à leur environnement virtuel respectif.

