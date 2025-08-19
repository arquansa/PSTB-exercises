import os
import datetime
import time # Pour simuler des pauses, comme un ordinateur qui "réfléchit"
# --- SIMULATION MCP : La Classe Contexte (pour les notifications de progrès) ---
class ContexteSimule:
     """
     Simule l'objet 'contexte' que les outils peuvent utiliser
     pour envoyer des notifications (comme ctx.info() en MCP).
     """
     def info(self, message):
         # TODO: Affichez le message précédé de "   [NOTIFICATION] "
        # Exemple : print(f"   [NOTIFICATION] {message}")
        # TODO: Ajoutez une petite pause pour simuler un traitement (0.5 secondes)
        # Utilisez time.sleep() ici.
        print(f"   [NOTIFICATION] {message}")
        time.sleep(0.5)
#
# --- SIMULATION MCP : Les Fonctions Outils (ce sont nos 'APIs' internes) ---
# Nous définirons nos outils ici à l'étape suivante.
def recherche_web_simulee(sujet_de_recherche):
    print(f"   -> Outil 'recherche_web_simulee' appelé pour : '{sujet_de_recherche}'")
    # TODO: Créez une liste d'au moins 2 dictionnaires.
    # Chaque dictionnaire doit avoir les clés "titre", "url", "texte".
    articles_trouves = [
        {
            "titre": "Les secrets d'une bonne hydratation",
            "url": "http://fauxsite.com/hydratation",
            "texte": "Boire de l'eau est essentiel pour notre corps. Cela aide à réguler la température corporelle, à transporter les nutriments et à éliminer les toxines. Pensez à boire régulièrement tout au long de la journée."
        },
        # TODO: Ajoutez un deuxième dictionnaire d'article ici
        {
            "titre": "L'importance du sommeil pour l'énergie",
            "url": "http://fauxsite.com/sommeil",
            "texte": "Un sommeil de qualité est crucial pour la récupération physique et mentale. Il influence directement notre humeur, notre concentration et notre système immunitaire. Établir une routine de sommeil peut grandement améliorer votre quotidien."
        }
    ]
    # TODO: Retournez un dictionnaire qui contient votre liste d'articles
    # La clé doit être "resultats". Exemple: {"resultats": articles_trouves}
    return {"resultats": articles_trouves}
def resumer_avec_llm_simule(sujet_du_briefing, liste_articles, ctx: ContexteSimule):
     # TODO: Appelez ctx.info() pour dire que le résumé commence
     # TODO: Ajoutez un time.sleep(1) pour simuler la réflexion
     ctx.info("Début du résumé avec le LLM simulé...")
     time.sleep(1)

     resume_texte = f"Briefing Généré (LLM Simulé) sur : {sujet_du_briefing}\n\n"
     resume_texte += "Points Clés (Générés) :\n"

     sources_pour_llm = []
     for i, article in enumerate(liste_articles):
         # TODO: Appelez ctx.info() pour dire que vous analysez l'article courant
         # TODO: Prenez la première phrase de l'article (voir l'astuce ci-dessus)
         ctx.info(f"Analyse de l'article {i+1}: {article['titre']}")
         premiere_phrase = article['texte'].split('. ')[0] + '.'
# TODO: Ajoutez cette phrase au resume_texte avec une indication de source
         # Exemple : resume_texte += f"- {premiere_phrase} [Source {i+1}]\n"
         resume_texte += f"- {premiere_phrase} [Source {i+1}]\n"
# TODO: Ajoutez les détails de la source à sources_pour_llm
         # Exemple : sources_pour_llm.append(f"[Source {i+1}] {article['titre']} - {article['url']}")
         sources_pour_llm.append(f"[Source {i+1}] {article['titre']} - {article['url']}")
# TODO: Ajoutez un time.sleep(0.3)
         time.sleep(0.3)

     resume_texte += "\nSources Utilisées :\n" + "\n".join(sources_pour_llm)
     # TODO: Appelez ctx.info() pour dire que le LLM a terminé
     # TODO: Retournez un dictionnaire avec la clé "briefing_complet"
     ctx.info("Résumé terminé.")
     return {"briefing_complet": resume_texte}

def enregistrer_fichier(nom_fichier, contenu_briefing):
     dossier_sortie = "briefings_generes"
     # TODO: Créez le dossier de sortie s'il n'existe pas
     # Utilisez os.makedirs()
     os.makedirs(dossier_sortie, exist_ok=True)

     chemin_complet = os.path.join(dossier_sortie, nom_fichier)
     try:
         # TODO: Ouvrez le fichier en mode écriture ('w') avec l'encodage 'utf-8'
        # TODO: Écrivez le contenu du briefing dans le fichier
        with open(chemin_complet, "w", encoding="utf-8") as f:
            f.write(contenu_briefing)


        print(f"   -> Outil 'enregistrer_fichier' : Briefing enregistré dans '{chemin_complet}'")
        # TODO: Retournez un dictionnaire avec la clé "chemin"
        return {"chemin": chemin_complet}
     except Exception as e:
         print(f"Erreur lors de l'enregistrement du briefing : {e}")
         return {"chemin": None}
     
def lister_outils_mcp_simule():
        print("   -> Outil 'lister_outils_mcp_simule' appelé.")
        outils_disponibles = [
         {"nom": "recherche_web_simulee", "description": "Recherche des articles sur un sujet donné."},
         # TODO: Ajoutez les autres outils que vous avez créés ici
         {"nom": "resumer_avec_llm_simule", "description": "Génère un résumé avec un LLM simulé et envoie des notifications."},
         {"nom": "enregistrer_fichier", "description": "Sauvegarde un contenu dans un fichier texte."},
    ]
        return {"outils": outils_disponibles}

if __name__ == "__main__":
    print("--- Démarrage du Client MCP Simulé ---")

    # --- Simulation MCP : Handshake (Poignée de Main) ---
    print("\nSIMULATION MCP : Effectuation du 'handshake' (établissement de la connexion)...")
    time.sleep(1) # Simule le temps du handshake
    print("SIMULATION MCP : Handshake terminé. La 'session' est établie.")

    # --- Simulation MCP : Découverte des outils ---
    print("\nSIMULATION MCP : Demande des outils disponibles au 'serveur'...")
    resultats_decouverte = lister_outils_mcp_simule()
    print("SIMULATION MCP : Outils 'découverts' :")
    for outil in resultats_decouverte['outils']:
        print(f" - {outil['nom']}: {outil['description']}")

    # --- Le workflow principal du Bot ---
    sujet_utilisateur = input("\nQuel sujet voulez-vous briefer (ex: 'écologie urbaine') ? ")
    if not sujet_utilisateur:
        sujet_utilisateur = "Sujet par défaut" # Mettez un sujet par défaut qui a du sens avec vos articles simulés
        print(f"Aucun sujet entré, utilisant le défaut : '{sujet_utilisateur}'")

    print(f"\nLe bot va générer un briefing pour : '{sujet_utilisateur}'")

    # 1. Appel de l'outil de recherche simulée
    print("\n1. Appel de l'outil 'recherche_web_simulee'...")
    result_recherche = recherche_web_simulee(sujet_utilisateur)
    articles = result_recherche.get('resultats', []) # Utilisez .get pour éviter les erreurs si la clé n'existe pas

    if not articles:
        print("   -> Aucun article simulé trouvé. Arrêt du processus.")
    else:
        print(f"   -> {len(articles)} articles trouvés simulés.")

        # 2. Appel de l'outil de résumé LLM simulé, en passant le CONTEXTE
        print("\n2. Appel de l'outil 'resumer_avec_llm_simule' (regardez les NOTIFICATIONS !) ...")
        # TODO: Créez une nouvelle instance de votre ContexteSimule() ici.
        # C'est cet objet que votre outil de résumé utilisera pour envoyer des notifications.
        contexte_pour_llm = ContexteSimule() # Remplacez None par votre instance

        result_resume = resumer_avec_llm_simule(sujet_utilisateur, articles, contexte_pour_llm)
        contenu_briefing = result_resume.get('briefing_complet', "Erreur: Contenu non généré.")

        # 3. Appel de l'outil d'enregistrement
        print("\n3. Appel de l'outil 'enregistrer_fichier'...")
        date_du_jour = datetime.date.today().isoformat()
        # Nettoyer le sujet pour le nom de fichier (supprimer espaces, caractères spéciaux)
        nom_fichier_propre = sujet_utilisateur.replace(' ', '_').replace("'", "").lower()
        nom_fichier_briefing = f"briefing_{nom_fichier_propre}_{date_du_jour}.txt"

        result_enregistrement = enregistrer_fichier(nom_fichier_briefing, contenu_briefing)
        chemin_final = result_enregistrement.get('chemin')

        print("\n--- Processus du Bot Intelligent Simulé Terminé ---")
        if chemin_final:
            print(f"Votre briefing est prêt ! Ouvrez le fichier : '{chemin_final}'")
        else:
            print("Une erreur est survenue lors de la création du briefing.")

