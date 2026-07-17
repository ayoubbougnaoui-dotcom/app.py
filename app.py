import streamlit as st

# 1. Configuration de la page du site
st.set_page_config(page_title="Générateur de CV", page_icon="📄", layout="centered")

st.title("🚀 Mon Générateur de CV en Ligne")
st.subheader("Crée ton profil et télécharge ton fichier en un clic !")

st.markdown("---")

# 2. Formulaire de saisie sur le site web
st.write("### 📝 Remplis tes informations :")

profil_cv = {}
profil_cv["prenom"] = st.text_input("Quel est ton prénom ?")
profil_cv["metier"] = st.text_input("Quel métier recherches-tu ?")
profil_cv["ville"] = st.text_input("Dans quelle ville habites-tu ?")

# 3. Bouton pour générer le CV
if st.button("✨ Générer mon CV"):
    # Vérification si un champ est vide
    if profil_cv["prenom"] == "" or profil_cv["metier"] == "" or profil_cv["ville"] == "":
        st.error("❌ Oups ! Tu as laissé une case vide. Remplis bien tout.")
    else:
        st.success(f"🎉 Bravo {profil_cv['prenom']} ! Ton profil est prêt.")
        
        # Création du texte du CV mis en page
        texte_cv = f"""===================================
           CV DE {profil_cv['prenom'].upper()} 
===================================

Métier recherché : {profil_cv['metier']}
Ville : {profil_cv['ville']}

Fait avec mon Générateur de CV en Python 💻
"""
        
        # Affichage d'un aperçu sur le site
        st.write("### 👁️ Aperçu de ton CV :")
        st.code(texte_cv)
        
        # Bouton magique pour télécharger le fichier directement depuis le site !
        st.download_button(
            label="💾 Télécharger mon CV (.txt)",
            data=texte_cv,
            file_name=f"CV_{profil_cv['prenom']}.txt",
            mime="text/plain"
        )
