import streamlit as st
import streamlit.components.v1 as components

# 1. Configuration de la page
st.set_page_config(page_title="Générateur de CV Pro", page_icon="📄", layout="centered")

# --- BARRE DE PROGRESSION (Calcul du remplissage) ---
st.markdown("""
    <style>
    .main-title { color: #1E3A8A; font-size: 32px; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .subtitle { color: #3B82F6; font-size: 18px; text-align: center; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🚀 Mon Générateur de CV Professionnel</div>', unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Créez un CV au design moderne et percutant en quelques instants</div>", unsafe_allow_html=True)

# 2. PERSONNALISATION DU THÈME
st.write("### 🎨 Personnalise le style de ton CV :")
theme = st.selectbox(
    "Choisis la couleur principale de ton CV :",
    ["Bleu Moderne 🔵", "Vert Émeraude 🟢", "Gris Minimaliste ⚫"]
)

# Définition des couleurs selon le thème choisi
if "Bleu" in theme:
    color_primary = "#1E3A8A"
    color_secondary = "#3B82F6"
    color_bg_contact = "#E5E7EB"
elif "Vert" in theme:
    color_primary = "#064E3B"
    color_secondary = "#10B981"
    color_bg_contact = "#D1FAE5"
else:
    color_primary = "#1F2937"
    color_secondary = "#4B5563"
    color_bg_contact = "#E5E7EB"

st.write("---")
st.write("### 📝 Remplis tes informations :")

# --- SECTION 1 : CONTACT ---
with st.expander("👤 1. Informations Personnelles & Contact", expanded=True):
    nom = st.text_input("Nom complet", value="Kylian Mbappé")
    titre_pro = st.text_input("Métier recherché / Titre du CV", value="Footballeur Professionnel / Attaquant International")
    email = st.text_input("Adresse e-mail", value="kylian.mbappe@example.com")
    telephone = st.text_input("Numéro de téléphone", value="06 07 10 29 09")
    ville = st.text_input("Ville & Code Postal", value="Bondy 93140")
    linkedin = st.text_input("Lien LinkedIn / Réseaux (Optionnel)", value="instagram.com/k.mbappe")

# --- SECTION 2 : ACCROCHE GÉNÉRÉE ---
with st.expander("📝 2. À propos de moi (Mots-clés)", expanded=False):
    mots_cles = st.text_input(
        "Entre tes points forts séparés par des virgules :",
        value="Rapide, Déterminé, Sens du collectif, Leadership"
    )
    if mots_cles:
        accroche = f"Professionnel {titre_pro.lower()} caractérisé par mon profil : {mots_cles.strip()}. Passionné par l'excellence et le travail bien fait, je mets mes compétences et mon esprit d'équipe au service d'objectifs ambitieux."
    else:
        accroche = "Profil professionnel motivé et rigoureux."

# --- SECTION 3 : EXPÉRIENCES ---
with st.expander("🏢 3. Expériences Professionnelles (Jusqu'à 3)", expanded=False):
    st.markdown("#### 🔹 Expérience 1")
    exp1_poste = st.text_input("Poste 1", value="Attaquant Star")
    exp1_entreprise = st.text_input("Club / Entreprise 1", value="Real Madrid CF")
    exp1_dates = st.text_input("Dates 1", value="2024 - Présent")
    exp1_missions = st.text_area("Missions 1 (une par ligne)", value="- Intégration de l'effectif professionnel et adaptation tactique\n- Inscription de buts décisifs en Liga et Ligue des Champions\n- Participation aux campagnes marketing internationales")

    st.markdown("---")
    st.markdown("#### 🔹 Expérience 2")
    exp2_poste = st.text_input("Poste 2", value="Meilleur Buteur de l'Histoire du Club")
    exp2_entreprise = st.text_input("Club / Entreprise 2", value="Paris Saint-Germain (PSG)")
    exp2_dates = st.text_input("Dates 2", value="2017 - 2024")
    exp2_missions = st.text_area("Missions 2", value="- Conquête de plusieurs titres de Champion de France\n- Leadership d'équipe sur le terrain en tant que vice-capitaine\n- Animation des attaques et gestion de la pression médiatique")

    st.markdown("---")
    st.markdown("#### 🔹 Expérience 3")
    exp3_poste = st.text_input("Poste 3", value="Révélation du Championnat")
    exp3_entreprise = st.text_input("Club / Entreprise 3", value="AS Monaco")
    exp3_dates = st.text_input("Dates 3", value="2015 - 2017")
    exp3_missions = st.text_area("Missions 3", value="- Formation d'excellence au centre de formation\n- Demi-finaliste de la Ligue des Champions à 18 ans\n- Champion de France de Ligue 1 (2017)")

# --- SECTION 4 : FORMATIONS ---
with st.expander("🎓 4. Formations & Diplômes (Jusqu'à 3)", expanded=False):
    st.markdown("#### 🎓 Formation 1")
    diplome1 = st.text_input("Diplôme 1", value="Baccalauréat STMG")
    ecole1 = st.text_input("École 1", value="Lycée de l'AS Monaco")
    dates1 = st.text_input("Année 1", value="2016")
    
    st.markdown("---")
    st.markdown("#### 🎓 Formation 2")
    diplome2 = st.text_input("Diplôme 2 (Optionnel)", value="Formation Management Sportif & Leadership")
    ecole2 = st.text_input("École 2", value="The Real Academy")
    dates2 = st.text_input("Année 2", value="2020")

    st.markdown("---")
    st.markdown("#### 🎓 Formation 3")
    diplome3 = st.text_input("Diplôme 3 (Optionnel)", value="")
    ecole3 = st.text_input("École 3", value="")
    dates3 = st.text_input("Année 3", value="")

# --- SECTION 5 : SKILLS ---
with st.expander("🛠️ 5. Compétences & Langues", expanded=False):
    competences = st.text_input("Compétences (séparées par des virgules)", value="Vitesse explosive, Finition devant le but, Dribbles, Leadership, Sang-froid")
    langues = st.text_input("Langues", value="Français (Maternelle), Espagnol (Courant), Anglais (Courant)")
    interets = st.text_input("Centres d'intérêt", value="Mode, Philantropie, Jeux vidéo, Tennis")

st.markdown("---")

# 3. BOUTON DE GÉNÉRATION
if st.button("✨ Générer mon CV Personnalisé"):
    if not nom or not titre_pro or not email:
        st.error("❌ Remplis au moins le Nom, le Titre et l'E-mail !")
    else:
        st.success("🎉 Ton superbe CV est prêt !")

        # Formations HTML dynamiques
        formations_html = f"<p><strong>{diplome1}</strong> – {ecole1} <span style='color:#666;'>({dates1})</span></p>"
        if diplome2:
            formations_html += f"<p style='margin-top:8px;'><strong>{diplome2}</strong> – {ecole2} <span style='color:#666;'>({dates2})</span></p>"
        if diplome3:
            formations_html += f"<p style='margin-top:8px;'><strong>{diplome3}</strong> – {ecole3} <span style='color:#666;'>({dates3})</span></p>"

        # Code HTML ultra-pro thématisé
        cv_html_page = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333; background-color: #ffffff; padding: 10px; }}
                .cv-container {{ max-width: 750px; margin: 0 auto; background-color: #FAFAFA; padding: 30px; border-radius: 8px; border-top: 10px solid {color_primary}; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }}
                h1 {{ color: {color_primary}; margin: 0; font-size: 30px; letter-spacing: -0.5px; }}
                h3 {{ color: {color_secondary}; margin: 5px 0 15px 0; font-weight: 400; font-style: italic; font-size: 18px; }}
                .contact-bar {{ font-size: 13px; background-color: {color_bg_contact}; padding: 10px; border-radius: 4px; margin-bottom: 20px; color: #1F2937; }}
                h4 {{ color: {color_primary}; border-bottom: 2px solid {color_secondary}; margin-top: 25px; padding-bottom: 5px; font-size: 14px; letter-spacing: 0.5px; text-transform: uppercase; }}
                p, div {{ font-size: 13px; line-height: 1.6; }}
                .job-title {{ font-weight: bold; color: #1F2937; }}
                .mission {{ font-size: 12.5px; white-space: pre-line; margin-left: 15px; color: #4B5563; margin-top: 5px; }}
            </style>
        </head>
        <body>
            <div class="cv-container">
                <h1>{nom}</h1>
                <h3>{titre_pro}</h3>
                
                <div class="contact-bar">
                    📍 {ville} &nbsp;|&nbsp; 📞 {telephone} &nbsp;|&nbsp; 📧 {email} &nbsp;|&nbsp; 🔗 {linkedin}
                </div>
                
                <h4>📖 Profil & Objectifs</h4>
                <p>{accroche}</p>
                
                <h4>💼 Parcours Professionnel</h4>
                <div>
                    <p><span class="job-title">{exp1_poste}</span> – {exp1_entreprise} <span style="color:#666; float:right;">{exp1_dates}</span></p>
                    <p class="mission">{exp1_missions}</p>
                    
                    <p style="margin-top: 15px;"><span class="job-title">{exp2_poste}</span> – {exp2_entreprise} <span style="color:#666; float:right;">{exp2_dates}</span></p>
                    <p class="mission">{exp2_missions}</p>
                    
                    <p style="margin-top: 15px;"><span class="job-title">{exp3_poste}</span> – {exp3_entreprise} <span style="color:#666; float:right;">{exp3_dates}</span></p>
                    <p class="mission">{exp3_missions}</p>
                </div>
                
                <h4>🎓 Formations & Diplômes</h4>
                <div>
                    {formations_html}
                </div>
                
                <h4>🛠️ Compétences & Langues</h4>
                <p><strong>Compétences clés :</strong> {competences}</p>
                <p><strong>Langues :</strong> {langues}</p>
                
                <h4>⚽ Centres d'intérêt</h4>
                <p>{interets}</p>
            </div>
        </body>
        </html>
        """

        # Rendu sur le site
        st.write("### 👁️ Ton CV Stylisé :")
        components.html(cv_html_page, height=750, scrolling=True)

        # Bouton de téléchargement de la page imprimable
        st.write("### 💾 Enregistre ton document :")
        st.download_button(
            label="📥 Télécharger la version Imprimable (Ouvrir puis Ctrl+P pour sauvegarder en PDF)",
            data=cv_html_page,
            file_name=f"CV_{nom.replace(' ', '_')}.html",
            mime="text/html",
            use_container_width=True
        )
        st.info("💡 **Pour avoir le PDF parfait :** Ouvre le fichier `.html` téléchargé, fais `Ctrl + P` (ou clic droit -> Imprimer) sur ton ordinateur, et sélectionne **'Enregistrer au format PDF'**.")
