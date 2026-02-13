"""
collect_vocals.py

Ce script regroupe les pistes vocales extraites par Demucs dans un dossier unique.

Pour chaque sous-dossier présent dans `data/vocals/htdemucs/`, le fichier `vocals.wav` est
copié dans le dossier `data/vocals_only/`. Les fichiers sont renommés à partir du nom
du dossier d'origine, après suppression des identifiants numériques initiaux, et le suffixe
`-vocals.wav` est ajouté.

L'objectif est d'obtenir un ensemble homogène de pistes vocales, prêtes à être utilisées
pour le calcul d'embeddings vocaux dans les étapes suivantes du projet.
"""

from pathlib import Path
import shutil

DEMUX_DIR = Path("data/vocals/htdemucs")
OUTPUT_DIR = Path("data/vocals_only")
OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    for track_dir in DEMUX_DIR.iterdir():
        if not track_dir.is_dir():
            continue

        vocals_path = track_dir / "vocals.wav"
        if not vocals_path.exists():
            continue

        # On enlève les 12 premiers caractères
        base_name = track_dir.name[12:]

        new_name = base_name + "-vocals.wav"
        dest_path = OUTPUT_DIR / new_name

        i = 2
        while dest_path.exists():
            dest_path = OUTPUT_DIR / f"{base_name}-vocals-{i}.wav"
            i += 1

        shutil.copy(vocals_path, dest_path)
        print("Copié :", dest_path.name)

    print("Terminé")

if __name__ == "__main__":
    main()