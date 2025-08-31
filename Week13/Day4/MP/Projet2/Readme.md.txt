# Projet R�seau - Syst�me de Traitement Multi-Agents

Ce projet contient **deux r�seaux** ind�pendants simulant des services backend distincts avec leurs propres environnements, serveurs, orchestrateurs, et interfaces utilisateur.

## Structure du Projet

Projet/
?
??? Projet1/
? ??? .venv-2/ # Environnement virtuel du 1er r�seau
? ??? src/
? ? ??? summarizer_server.py # Serveur FastAPI (r�seau 1)
? ? ??? agent.py # Orchestrateur (r�seau 1)
? ??? app.py # Interface Streamlit (r�seau 1) ==> OK fonctionnelle
??? Projet2/
? ??? .venv/ # Environnement virtuel du 2e r�seau
? ??? src/
? ? ??? main_server.py # Serveur FastAPI (r�seau 2)
? ? ??? agent_orchest.py # Orchestrateur (r�seau 2)
? ??? app_2.py # Interface Streamlit (r�seau 2) ==>  (non fonctionnelle/facultative)
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
uvicorn summarizer_server:app --host 0.0.0.0 --port 5000 �reload

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

Lancer l�interface utilisateur (Streamlit)
Projet 1

cd Projet1
streamlit run app.py (fonctionnelle)

Projet 2
cd Projet2
streamlit run app_2.py (non fonctionnelle)

Outils utiles
V�rification des ports
- Tester si un serveur fonctionne :
curl http://localhost:5000  # ou 8000 selon le projet

- Lister les ports ouverts :
netstat -an | find "LISTEN"

Gestion des d�pendances
- Installer les  biblioth�ques : pip install -r requirements.txt
-  Mettre � jour requirements.txt : pip freeze > requirements.txt
- Lister les paquets install�s :pip list

Notes
- Il est recommand� d�utiliser Visual Studio Code et d�ouvrir deux fen�tres ind�pendantes (Ctrl+Shift+N) pour isoler les deux environnements.
- Les serveurs doivent �tre lanc�s dans la console activ�e correspondant � leur environnement virtuel respectif.

