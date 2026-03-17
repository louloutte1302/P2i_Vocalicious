import numpy as np
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from extract_feat_vocals import extract_voice_features
from navigate import clear

def recommend(vocal_to_analyse):

    # Extraire features utilisateur
    user_features, pitch_label = extract_voice_features(str(vocal_to_analyse))

    if user_features is None:
        print("Pas de voix détectée.\n")
        return

    # Charger le catalogue
    catalog_path = Path("data/catalog.npy")
    names_path = Path("data/catalog_names.txt")

    if not catalog_path.exists():
        print("Catalogue introuvable ! Lance d'abord : python src/create_catalog_once.py")
        return

    if not names_path.exists():
        print("Fichier des noms introuvable !")
        return

    X = np.load(catalog_path)

    with open(names_path, "r", encoding="utf-8") as f:
        names = [line.strip() for line in f]

    
    # Normaliser
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    u_scaled = scaler.transform(user_features.reshape(1, -1))

    # Calcul similarité
    sims = cosine_similarity(u_scaled, X_scaled)[0]
    best_idx = np.argsort(-sims)[:5]

    recommended_names = [names[i] for i in best_idx]

    # Afficher
    clear()
    print("\n==============================")
    print("\n ✓ Analyse terminée ")
    print("\n==============================")
    print("\n Extrait de voix analysé :", vocal_to_analyse.name)
    print("\n Tessiture estimée :", pitch_label)
    print("\n Votre Top 5 des musique:")
    
    
    for i in best_idx:
        print("x", names[i], "| score =", round(float(sims[i]), 3))
    
    return recommended_names