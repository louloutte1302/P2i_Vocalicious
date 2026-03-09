import numpy as np
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

from extract_feat_vocals import extract_voice_features
from navigate import pick_file  


def recommend(vocal_to_analyse):
    # 1) Charger le catalogue déjà calculé
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

    # Extraire features utilisateur
    user_features, pitch_label = extract_voice_features(str(vocal_to_analyse))
    if user_features is None:
        print("Pas de voix détectée.")
        return

    # 4) Normaliser + comparer (cosine)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    u_scaled = scaler.transform(user_features.reshape(1, -1))

    sims = cosine_similarity(u_scaled, X_scaled)[0]
    best_idx = np.argsort(-sims)[:5]

    # 5) Afficher
    print("\n==============================")
    print("\nExtrait :", vocal_to_analyse.name)
    print("Tessiture estimée :", pitch_label)
    print("Top 5 :")
    for i in best_idx:
        print("-", names[i], "| score =", round(float(sims[i]), 3))