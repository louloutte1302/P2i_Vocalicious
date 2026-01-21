Un venv (virtual environment) est un environnement Python isolé pour un projet.

👉 C’est comme une bulle :

ton projet vit dedans

ses bibliothèques sont dedans


# Vocalicious 🎤🎵

Recommandation musicale basée sur la similarité vocale.

## Pipeline
1. Séparation voix/instrument (Demucs)
2. Extraction d'embeddings vocaux (SpeechBrain ECAPA)
3. Recherche par similarité cosinus
4. Recommandation Top-K

## Installation
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
