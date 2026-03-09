import numpy as np
from pathlib import Path
from tqdm import tqdm 
from extract_feat_vocals import extract_voice_features

"""
build_catalog.py

Construit un catalogue de caractéristiques audio à partir des fichiers
présents dans le dossier `data/vocals_30sec`.

Pour chaque fichier audio :
    - les features vocales sont extraites via `extract_voice_features`
    - le vecteur de caractéristiques est ajouté à une matrice globale

Les résultats sont sauvegardés dans :
    - `data/catalog.npy` : matrice numpy contenant les vecteurs de features
    - `data/catalog_names.txt` : noms des fichiers correspondant aux vecteurs

Ce catalogue est ensuite utilisé par recommend.py pour
comparer un extrait vocal utilisateur avec les enregistrements dans la matrice.

La barre de progression `tqdm` permet de suivre l'avancement de
l'extraction des features.

"""

folder = Path("data/vocals_30sec")
files = [f for f in folder.iterdir() if f.is_file()]
files.sort()

names = []
vectors = []

# tqdm enveloppe la liste des fichiers == barre de progresions
for f in tqdm(files, desc="Extraction des features"):
    features, _ = extract_voice_features(str(f))
    if features is None:
        continue

    names.append(f.name)
    vectors.append(features)

if len(vectors) == 0:
    print("Aucun fichier exploitable.")
    raise SystemExit

X = np.vstack(vectors)

np.save("data/catalog.npy", X)

with open("data/catalog_names.txt", "w") as f:
    for name in names:
        f.write(name + "\n")

print("\n Catalogue créé.")