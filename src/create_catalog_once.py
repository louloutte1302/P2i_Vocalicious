import numpy as np
from pathlib import Path
from tqdm import tqdm 
from extract_feat_vocals import extract_voice_features

folder = Path("data/vocals_only")
files = [f for f in folder.iterdir() if f.is_file()]
files.sort()

names = []
vectors = []

# tqdm enveloppe la liste des fichiers
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