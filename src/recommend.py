import sys
import numpy as np
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

from extract_feat import extract_voice_features


AUDIO_EXTS = {".wav", ".mp3", ".flac", ".m4a"}


def list_audio_files(folder_path):
    folder = Path(folder_path)
    files = []

    for f in folder.iterdir():
        if f.is_file() and f.suffix.lower() in AUDIO_EXTS:
            files.append(f)

    return files


def build_feature_matrix(folder_path):
    files = list_audio_files(folder_path)

    names = []
    vectors = []

    for f in files:
        features, _ = extract_voice_features(str(f))
        if features is None:
            continue

        names.append(f.name)
        vectors.append(features)

    if len(vectors) == 0:
        raise ValueError("Aucun fichier exploitable.")

    X = np.vstack(vectors)
    return X, names


def top_k_recommend(user_vector, catalog_matrix, catalog_names, k=5):
    scaler = StandardScaler()

    catalog_scaled = scaler.fit_transform(catalog_matrix)
    user_scaled = scaler.transform(user_vector.reshape(1, -1))

    sims = cosine_similarity(user_scaled, catalog_scaled)[0]
    best_indices = np.argsort(-sims)[:k]

    results = []
    for idx in best_indices:
        results.append((catalog_names[idx], float(sims[idx])))

    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python compare_voice.py NOM_FICHIER.wav")
        return

    user_file_name = sys.argv[1]

    user_path = Path("data/vocals_to_analyse") / user_file_name
    catalog_folder = "data/vocals_only"

    # 1️⃣ Extraire features utilisateur
    user_features, pitch_label = extract_voice_features(str(user_path))

    if user_features is None:
        print("Pas de voix détectée.")
        return

    # 2️⃣ Construire matrice catalogue
    catalog_matrix, catalog_names = build_feature_matrix(catalog_folder)

    # 3️⃣ Comparer
    results = top_k_recommend(user_features, catalog_matrix, catalog_names, k=5)

    print("\nVoix détectée comme :", pitch_label)
    print("Top 5 recommandations :")
    for name, score in results:
        print("-", name, "| score =", round(score, 3))


if __name__ == "__main__":
    main()