import streamlit as st

# 1. Configuration de la page du site
st.set_page_config(page_title="Mon Générateur de CV", page_icon="📄", layout="centered")

# Style CSS pour rendre le site et l'aperçu encore plus beaux avec de la couleur
st.markdown("""
    <style>
    .main-title { color: #1E3A8A; font-size: 32px; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .subtitle { color: #3B82F6; font-size: 18px; text-align: center; margin-bottom: 25px; }
    .section-header { color: #1E3A8A; border-bottom: 2px solid #3B82F6; padding-bottom: 5px; margin-top: 20px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# Titre principal mis à jour
st.markdown('<div class="main-title">✨ Mon Générateur de CV</div>', unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Remplis tes informations et télécharge ton CV complet en un clic !</div>", unsafe_allow_html=True)

st.write("### 📝 Remplis les différentes sections de ton CV :")

# --- SECTION 1 : INFORMATIONS PERSONNELLES (Avec Kylian Mbappé) ---
with st.expander("👤 1. Informations Personnelles & Contact", expanded=True):
    nom = st.text_input("Nom complet (Prénom & Nom)", value="Kylian Mbappé")
    titre_pro = st.text_input("Titre du CV / Métier recherché", value="Footballeur Professionnel / Attaquant International")
    email = st.text_input("Adresse e-mail", value="kylian.mbappe@example.com")
    telephone = st.text_input("Numéro de téléphone", value="06 07 10 29 09")
    ville = st.text_input("Ville & Code Postal", value="Madrid, Espagne (Originaire de Bondy)")
    linkedin = st.text_input("Lien LinkedIn ou Site Web (Optionnel)", value="instagram.com/k.mbappe")

# --- SECTION 2 : ACCROCHE ---
with st.expander("📝 2. À propos de moi (Accroche)", expanded=False):
    accroche = st.text_area(
        "Présente ton profil en quelques phrases percutantes :",
        value="Attaquant d'élite déterminé, rapide et doté d'un grand sens du collectif. Passionné par l'excellence et la victoire, je mets ma technique, mon leadership et mon esprit de compétition au service des plus grands objectifs sportifs."
    )

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
with st.expander("🎓 4. Formations & Diplômes", expanded=False):
    st.write("#### Dernier diplôme ou formation")
    diplome = st.text_input("Nom du diplôme / Titre de la formation", value="Baccalauréat STMG (Sciences et Technologies du Management et de la Gestion)")
    ecole = st.text_input("Établissement / École", value="Lycée privé sous contrat avec l'AS Monaco")
    formation_dates = st.text_input("Période / Année d'obtention", value="2016")

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
        st.success("🎉 Ton CV a été généré avec succès ! Découvre l'aperçu stylisé ci-dessous.")

        # 1. Version Texte pour le téléchargement (.txt)
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

🎓 FORMATION
------------------------------------------------------------------------
• {formation_dates} | {diplome}
  🏢 {ecole}

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

        # 2. Affichage d'un aperçu coloré et mis en page en HTML directement sur le site
        st.write("### 👁️ Aperçu de ton nouveau CV :")
        
        cv_html = f"""
        <div style="background-color: #F3F4F6; padding: 25px; border-radius: 10px; border-left: 8px solid #1E3A8A; font-family: sans-serif; color: #333;">
            <h1 style="color: #1E3A8A; margin-bottom: 0; padding-bottom: 0;">{nom}</h1>
            <h3 style="color: #3B82F6; margin-top: 5px; font-weight: normal; font-style: italic;">{titre_pro}</h3>
            
            <p style="font-size: 14px; background-color: #E5E7EB; padding: 10px; border-radius: 5px;">
                📍 {ville} | 📞 {telephone} | 📧 {email} | 🔗 {linkedin}
            </p>
            
            <h4 style="color: #1E3A8A; border-bottom: 1px solid #1E3A8A; margin-top: 20px; padding-bottom: 3px;">📖 PROFIL</h4>
            <p style="font-size: 15px; line-height: 1.5;">{accroche}</p>
            
            <h4 style="color: #1E3A8A; border-bottom: 1px solid #1E3A8A; margin-top: 20px; padding-bottom: 3px;">💼 EXPÉRIENCES PROFESSIONNELLES</h4>
            <p><strong>{exp1_poste}</strong> - {exp1_entreprise} <span style="color:#666;">({exp1_dates})</span></p>
            <p style="font-size: 14px; white-space: pre-line; margin-left: 15px;">{exp1_missions}</p>
            
            <p style="margin-top: 15px;"><strong>{exp2_poste}</strong> - {exp2_entreprise} <span style="color:#666;">({exp2_dates})</span></p>
            <p style="font-size: 14px; white-space: pre-line; margin-left: 15px;">{exp2_missions}</p>
            
            <p style="margin-top: 15px;"><strong>{exp3_poste}</strong> - {exp3_entreprise} <span style="color:#666;">({exp3_dates})</span></p>
            <p style="font-size: 14px; white-space: pre-line; margin-left: 15px;">{exp3_missions}</p>
            
            <h4 style="color: #1E3A8A; border-bottom: 1px solid #1E3A8A; margin-top: 20px; padding-bottom: 3px;">🎓 FORMATION</h4>
            <p><strong>{diplome}</strong> – {ecole} <span style="color:#666;">({formation_dates})</span></p>
            
            <h4 style="color: #1E3A8A; border-bottom: 1px solid #1E3A8A; margin-top: 20px; padding-bottom: 3px;">🛠️ COMPÉTENCES & LANGUES</h4>
            <p style="font-size: 15px;"><strong>Compétences :</strong> {competences}</p>
            <p style="font-size: 15px;"><strong>Langues :</strong> {langues}</p>
            
            <h4 style="color: #1E3A8A; border-bottom: 1px solid #1E3A8A; margin-top: 20px; padding-bottom: 3px;">⚽ CENTRES D'INTÉRÊT</h4>
            <p style="font-size: 15px;">{interets}</p>
        </div>
        """
        st.markdown(cv_html, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        # Bouton pour télécharger le fichier texte propre
        st.download_button(
            label="💾 Télécharger mon CV au format (.txt)",
            data=cv_txt,
            file_name=f"CV_{nom.replace(' ', '_')}.txt",
            mime="text/plain"
        )
