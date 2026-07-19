import streamlit as st
import streamlit.components.v1 as components
import base64

# 1. Configuration de la page du site
st.set_page_config(page_title="Mon Générateur de CV", page_icon="📄", layout="centered")

# Style CSS pour le design global du site
st.markdown("""
    <style>
    .main-title { color: #1E3A8A; font-size: 32px; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .subtitle { color: #3B82F6; font-size: 18px; text-align: center; margin-bottom: 25px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">✨ Mon Générateur de CV</div>', unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Remplis tes informations et télécharge ton CV complet en un clic !</div>", unsafe_allow_html=True)

st.write("### 📝 Remplis les différentes sections de ton CV :")

# --- SECTION 1 : INFORMATIONS PERSONNELLES ---
with st.expander("👤 1. Informations Personnelles & Contact", expanded=True):
    nom = st.text_input("Nom complet (Prénom & Nom)", value="Kylian Mbappé")
    titre_pro = st.text_input("Titre du CV / Métier recherché", value="Footballeur Professionnel / Attaquant International")
    email = st.text_input("Adresse e-mail", value="kylian.mbappe@example.com")
    telephone = st.text_input("Numéro de téléphone", value="06 07 10 29 09")
    ville = st.text_input("Ville & Code Postal", value="Bondy 93140")
    linkedin = st.text_input("Lien LinkedIn ou Site Web", value="instagram.com/k.mbappe")

# --- SECTION 2 : ACCROCHE GÉNÉRÉE AUTOMATIQUEMENT ---
with st.expander("📝 2. À propos de moi (Génération Profil)", expanded=False):
    mots_cles = st.text_input(
        "Entre quelques mots-clés pour ton profil (séparés par des virgules) :",
        value="Rapide, Déterminé, Sens du collectif, Leadership"
    )
    
    if mots_cles:
        accroche = f"Professionnel {titre_pro.lower()} caractérisé par mon profil : {mots_cles.strip()}. Passionné par l'excellence et le travail bien fait, je mets mes compétences et mon esprit d'équipe au service d'objectifs ambitieux."
    else:
        accroche = "Profil professionnel motivé et rigoureux."

# --- SECTION 3 : EXPÉRIENCES ---
with st.expander("🏢 3. Expériences Professionnelles (Jusqu'à 3)", expanded=False):
    st.markdown("#### 🔹 Expérience 1 (La plus récente)")
    exp1_poste = st.text_input("Intitulé du poste 1", value="Attaquant Star")
    exp1_entreprise = st.text_input("Entreprise / Club 1", value="Real Madrid CF")
    exp1_dates = st.text_input("Période (Dates) 1", value="2024 - Présent")
    exp1_missions = st.text_area("Missions 1 (une par ligne)", value="- Intégration de l'effectif professionnel et adaptation tactique\n- Inscription de buts décisifs en Liga et Ligue des Champions\n- Participation aux campagnes marketing internationales du club")

    st.markdown("---")
    st.markdown("#### 🔹 Expérience 2")
    exp2_poste = st.text_input("Intitulé du poste 2", value="Meilleur Buteur de l'Histoire du Club")
    exp2_entreprise = st.text_input("Entreprise / Club 2", value="Paris Saint-Germain (PSG)")
    exp2_dates = st.text_input("Période (Dates) 2", value="2017 - 2024")
    exp2_missions = st.text_area("Missions 2 (une par ligne)", value="- Conquête de plusieurs titres de Champion de France (Ligue 1)\n- Leadership d'équipe sur le terrain en tant que vice-capitaine\n- Animation des attaques et gestion de la pression médiatique")

    st.markdown("---")
    st.markdown("#### 🔹 Expérience 3")
    exp3_poste = st.text_input("Intitulé du poste 3", value="Révélation du Championnat")
    exp3_entreprise = st.text_input("Entreprise / Club 3", value="AS Monaco")
    exp3_dates = st.text_input("Période (Dates) 3", value="2015 - 2017")
    exp3_missions = st.text_area("Missions 3 (une par ligne)", value="- Formation d'excellence au centre de formation\n- Demi-finaliste de la Ligue des Champions à 18 ans\n- Champion de France de Ligue 1 (2017)")

# --- SECTION 4 : FORMATIONS ---
with st.expander("🎓 4. Formations & Diplômes (Jusqu'à 3)", expanded=False):
    st.markdown("#### 🎓 Formation 1 (La plus récente)")
    diplome1 = st.text_input("Nom du diplôme 1", value="Baccalauréat STMG")
    ecole1 = st.text_input("Établissement / École 1", value="Lycée privé sous contrat avec l'AS Monaco")
    dates1 = st.text_input("Année d'obtention 1", value="2016")
    
    st.markdown("---")
    st.markdown("#### 🎓 Formation 2")
    diplome2 = st.text_input("Nom du diplôme 2 (Optionnel)", value="Formation Management Sportif & Leadership")
    ecole2 = st.text_input("Établissement / École 2", value="The Real Academy en ligne")
    dates2 = st.text_input("Année d'obtention 2", value="2020")

    st.markdown("---")
    st.markdown("#### 🎓 Formation 3")
    diplome3 = st.text_input("Nom du diplôme 3 (Optionnel)", value="")
    ecole3 = st.text_input("Établissement / École 3", value="")
    dates3 = st.text_input("Année d'obtention 3", value="")

# --- SECTION 5 : COMPÉTENCES & LANGUES ---
with st.expander("🛠️ 5. Compétences, Langues & Intérêts", expanded=False):
    competences = st.text_input("Compétences clés (séparées par des virgules)", value="Vitesse explosive, Finition devant le but, Dribbles, Leadership, Sang-froid, Esprit d'équipe")
    langues = st.text_input("Langues parlées (et niveau)", value="Français (Maternelle), Espagnol (Courant), Anglais (Courant)")
    interets = st.text_input("Centres d'intérêt", value="Mode, Philantropie (Association Inspired by KM), Jeux vidéo, Tennis")

st.markdown("---")

# 3. BOUTON DE GÉNÉRATION
if st.button("✨ Générer et Prévisualiser mon CV"):
    if not nom or not titre_pro or not email:
        st.error("❌ Les champs 'Nom complet', 'Titre du CV' et 'Adresse e-mail' sont obligatoires.")
    else:
        st.success("🎉 Ton CV a été généré avec succès ! Découvre l'aperçu et télécharge tes fichiers ci-dessous.")

        # Construction de la section Formations en texte (.txt)
        formations_txt = f"• {dates1} | {diplome1}\n  🏢 {ecole1}"
        if diplome2:
            formations_txt += f"\n\n• {dates2} | {diplome2}\n  🏢 {ecole2}"
        if diplome3:
            formations_txt += f"\n\n• {dates3} | {diplome3}\n  🏢 {ecole3}"

        # 1. Version Texte brute
        cv_txt = f"""========================================================================
{nom.upper()}
{titre_pro.upper()}
========================================================================

📌 CONTACT
------------------------------------------------------------------------
📍 Adresse : {ville}
📞 Tél     : {telephone}
📧 E-mail  : {email}
🔗 Liens   : {linkedin}

📖 PROFIL
------------------------------------------------------------------------
{accroche}

💼 EXPÉRIENCES PROFESSIONNELLES
------------------------------------------------------------------------
• {exp1_dates} | {exp1_poste}
  {exp1_entreprise}
  {exp1_missions}

• {exp2_dates} | {exp2_poste}
  {exp2_entreprise}
  {exp2_missions}

• {exp3_dates} | {exp3_poste}
  {exp3_entreprise}
  {exp3_missions}

🎓 FORMATIONS
------------------------------------------------------------------------
{formations_txt}

🛠️ COMPÉTENCES
------------------------------------------------------------------------
{competences}

🗣️ LANGUES
------------------------------------------------------------------------
{langues}

⚽ CENTRES D'INTÉRÊT
------------------------------------------------------------------------
{interets}

========================================================================
Généré automatiquement via l'application CV Python de {nom}
"""

        # Construction de la section Formations en HTML
        formations_html = f"<p><strong>{diplome1}</strong> – {ecole1} <span style='color:#666;'>({dates1})</span></p>"
        if diplome2:
            formations_html += f"<p style='margin-top:10px;'><strong>{diplome2}</strong> – {ecole2} <span style='color:#666;'>({dates2})</span></p>"
        if diplome3:
            formations_html += f"<p style='margin-top:10px;'><strong>{diplome3}</strong> – {ecole3} <span style='color:#666;'>({dates3})</span></p>"

        # Code HTML complet du CV conçu pour être imprimable proprement
        cv_html_page = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ font-family: sans-serif; color: #333; background-color: #ffffff; padding: 20px; }}
                .cv-card {{ max-width: 800px; margin: 0 auto; background-color: #F3F4F6; padding: 25px; border-radius: 10px; border-left: 8px solid #1E3A8A; }}
                h1 {{ color: #1E3A8A; margin-bottom: 0; padding-bottom: 0; font-size: 28px; }}
                h3 {{ color: #3B82F6; margin-top: 5px; font-weight: normal; font-style: italic; font-size: 18px; }}
                .contact-bar {{ font-size: 13px; background-color: #E5E7EB; padding: 10px; border-radius: 5px; margin-top: 10px; }}
                h4 {{ color: #1E3A8A; border-bottom: 2px solid #1E3A8A; margin-top: 20px; padding-bottom: 3px; font-size: 15px; text-transform: uppercase; }}
                p, div {{ font-size: 13px; line-height: 1.5; }}
                .mission {{ font-size: 12px; white-space: pre-line; margin-left: 15px; color: #4B5563; }}
                @media print {{
                    body {{ padding: 0; background: white; }}
                    .cv-card {{ border-radius: 0; padding: 0; background: transparent; border-left: 4px solid #1E3A8A; }}
                }}
            </style>
        </head>
        <body>
            <div class="cv-card">
                <h1>{nom}</h1>
                <h3>{titre_pro}</h3>
                
                <div class="contact-bar">
                    📍 {ville} | 📞 {telephone} | 📧 {email} | 🔗 {linkedin}
                </div>
                
                <h4>📖 PROFIL</h4>
                <p>{accroche}</p>
                
                <h4>💼 EXPÉRIENCES PROFESSIONNELLES</h4>
                <div>
                    <p><strong>{exp1_poste}</strong> - {exp1_entreprise} <span style="color:#666;">({exp1_dates})</span></p>
                    <p class="mission">{exp1_missions}</p>
                    
                    <p style="margin-top: 15px;"><strong>{exp2_poste}</strong> - {exp2_entreprise} <span style="color:#666;">({exp2_dates})</span></p>
                    <p class="mission">{exp2_missions}</p>
                    
                    <p style="margin-top: 15px;"><strong>{exp3_poste}</strong> - {exp3_entreprise} <span style="color:#666;">({exp3_dates})</span></p>
                    <p class="mission">{exp3_missions}</p>
                </div>
                
                <h4>🎓 FORMATIONS & DIPLÔMES</h4>
                <div>
                    {formations_html}
                </div>
                
                <h4>🛠️ COMPÉTENCES & LANGUES</h4>
                <p><strong>Compétences :</strong> {competences}</p>
                <p><strong>Langues :</strong> {langues}</p>
                
                <h4>⚽ CENTRES D'INTÉRÊT</h4>
                <p>{interets}</p>
            </div>
        </body>
        </html>
        """

        # --- APERÇU SUR LE SITE ---
        st.write("### 👁️ Aperçu de ton CV :")
        components.html(cv_html_page, height=600, scrolling=True)
        st.markdown("<br>", unsafe_allow_html=True)

        # --- BOUTONS DE TÉLÉCHARGEMENT OFFICIELS STREAMLIT ---
        st.write("### 💾 Liens de téléchargement :")
        
        # Colonnes pour mettre les boutons côte à côte proprement
        col1, col2 = st.columns(2)
        
        with col1:
            st.download_button(
                label="📄 Télécharger mon CV au format (.txt)",
                data=cv_txt,
                file_name=f"CV_{nom.replace(' ', '_')}.txt",
                mime="text/plain",
                use_container_width=True
            )
            
        with col2:
            # Création du bouton de téléchargement pour le format imprimable / Web (valable comme PDF)
            st.download_button(
                label="🌐 Télécharger la version Imprimable (Ouvrir & Enregistrer en PDF)",
                data=cv_html_page,
                file_name=f"CV_{nom.replace(' ', '_')}.html",
                mime="text/html",
                use_container_width=True
            )
            st.info("💡 **Astuce PDF :** Une fois le fichier imprimable téléchargé, ouvre-le dans ton navigateur et fais `Ctrl + P` (ou Imprimer) puis choisis **'Enregistrer au format PDF'**.")
