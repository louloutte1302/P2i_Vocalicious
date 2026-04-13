import numpy as np
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from extract_feat_vocals import extract_voice_features

def recommend(vocal_to_analyse):
    user_features, pitch_label = extract_voice_features(str(vocal_to_analyse))

    if user_features is None:
        return []

    catalog_path = Path("data/catalog.npy")
    names_path = Path("data/catalog_names.txt")

    if not catalog_path.exists():
        raise FileNotFoundError("Catalogue introuvable.")
    if not names_path.exists():
        raise FileNotFoundError("Fichier des noms introuvable.")

    X = np.load(catalog_path)

    with open(names_path, "r", encoding="utf-8") as f:
        names = [line.strip() for line in f]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    u_scaled = scaler.transform(user_features.reshape(1, -1))

    sims = cosine_similarity(u_scaled, X_scaled)[0]
    best_idx = np.argsort(-sims)[:5]

    recommended_names = [names[i] for i in best_idx]
    return recommended_names