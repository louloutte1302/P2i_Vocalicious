from .extract_feat_vocals import *
from pathlib import Path

def list_files(folder_path):
    """
    Liste tous les fichiers d'un dossier (sans filtrer par extension).
    """
    folder = Path(folder_path)
    files = [f for f in folder.iterdir() if f.is_file()]
    files.sort()
    return files


def build_feature_matrix(folder_path):
    """
    Calcule les features pour tous les fichiers d'un dossier.
    Renvoie :
      - X : matrice (N, D)
      - names : liste des noms de fichiers (N)
    """
    files = list_files(folder_path)

    names = []
    vectors = []

    for f in files:
        features, _ = extract_voice_features(str(f))

        # si pas de voix détectée, on ignore ce fichier
        if features is None:
            continue

        names.append(f.name)
        vectors.append(features)

    if len(vectors) == 0:
        raise ValueError(f"Aucun fichier exploitable dans {folder_path}")

    X = np.vstack(vectors)
    return X, names