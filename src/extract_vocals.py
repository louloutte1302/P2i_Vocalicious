"""
extract_vocals.py

Ce script permet d'extraire automatiquement la piste vocale d'un ensemble de fichiers audio
à l'aide du modèle de séparation de sources Demucs.

Les fichiers audio (mp3, wav, flac, m4a) doivent être placés dans le dossier `data/raw_tracks/`.
Pour chaque fichier, Demucs est exécuté afin de séparer la voix du reste de l'accompagnement musical.

Les résultats sont stockés dans `data/vocals/htdemucs/`, avec un sous-dossier par musique
contenant notamment le fichier `vocals.wav`.

Ce script constitue la première étape du pipeline de traitement audio du projet.
"""


from pathlib import Path
import subprocess

# Extensions audio acceptées
AUDIO_EXTS = {".mp3", ".wav", ".flac", ".m4a"}

# Dossiers
INPUT_DIR = Path("data/raw_tracks")
OUTPUT_DIR = Path("data/vocals")

# Modèle Demucs deeplearning qui sépare la voix des musiques
MODEL = "htdemucs"


def extract_vocals(audio_path: Path):
    """
    Lance Demucs pour extraire uniquement la piste 'vox' des fichiers audios.
    """
    cmd = [
        "demucs",
        "-n", MODEL,
        "--two-stems=vocals",
        "-o", str(OUTPUT_DIR),
        str(audio_path)
    ]
    subprocess.run(cmd, check=True)


def main():
    if not INPUT_DIR.exists():
        print(f"Le dossier {INPUT_DIR} n'existe pas.")
        return

    # Liste les fichiers audio dans data/raw_tracks
    files = [f for f in INPUT_DIR.iterdir() if f.suffix.lower() in AUDIO_EXTS]

    if not files:
        print(f"Aucun fichier audio trouvé dans votre BDD {INPUT_DIR}.")
        print("Ajouter des .mp3 / .wav / .flac / .m4a")
        return

    for f in files:
        extract_vocals(f)

    print("\nTerminé")
    print("Résultats des audios extraits dans : data/vocals/htdemucs/<nom_du_fichier>/vocals.wav")


if __name__ == "__main__":
    main()