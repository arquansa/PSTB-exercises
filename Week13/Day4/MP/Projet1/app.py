import streamlit as st
import requests

st.set_page_config(page_title="Résumé via Agent MCP", page_icon="🧠")
st.title("🧠 Résumeur de texte via Agent MCP")

user_input = st.text_area("Texte à résumer", height=200)

if st.button("Résumer"):
    if user_input.strip() == "":
        st.warning("Merci d’entrer un texte.")
    else:
        with st.spinner("En cours..."):
            try:
                response = requests.post("http://localhost:5000/infer/summarizer", json={"input": user_input})
                response.raise_for_status()
                summary = response.json().get("output", "[Aucun résumé généré]")
                st.success("Résumé :")
                st.write(summary)
            except Exception as e:
                st.error(f"Erreur lors de l’appel au serveur : {e}")

           # st.write(response.json()["output"])
