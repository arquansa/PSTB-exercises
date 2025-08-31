import streamlit as st
import subprocess
import sys
from dotenv import load_dotenv

st.title("Agent MCP multi-outils")

task = st.text_area("Que voulez-vous faire ? (ex: Nettoie ce texte puis analyse le sentiment)")

if st.button("Lancer"):
    if task.strip() == "":
        st.warning("Veuillez entrer une tâche.")
    else:
        with st.spinner("Execution..."):
            from pathlib import Path
         
            chemin_relatif = Path("agent_orchest.py")
            chemin_absolu = chemin_relatif.resolve()
            print("Chemin absolu :", chemin_absolu)
            print("Chemin relatif :", chemin_relatif)
            #result = subprocess.run(["python", chemin_absolu], input=task.encode(), capture_output=True)
            #result = subprocess.run(["python", "src/agent_orchest.py"], input=task.encode(), capture_output=True)
            result = subprocess.run(
                 [sys.executable, str(chemin_absolu), task],
                 capture_output=True,
                 text=True
            )
            st.subheader("Résultat :")
            st.code(result.stdout)
            if result.stderr:
                 st.subheader("Erreurs :")
                 st.code(result.stderr)
            #result = subprocess.run(["python", str(chemin_absolu), task], capture_output=True)
            st.success("Résultat obtenu :")
            st.code(result.stdout.decode(), language="text")
            if result.stderr: 
                 st.error("Erreur rencontrée :")
                 st.code(result.stderr.decode(), language="bash")
            #st.text(result.stdout.decode())
