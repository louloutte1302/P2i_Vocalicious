Un venv (virtual environment) est un environnement Python isolé pour un projet.

👉 C’est comme une bulle :

ton projet vit dedans

ses bibliothèques sont dedans



## Installation

# Vocalicious 🎤🎵

Recommandation musicale basée sur la similarité vocale.

## Pipeline
1. Séparation voix/instrument (Demucs)
2. Extraction d'embeddings vocaux (SpeechBrain ECAPA)
3. Recherche par similarité cosinus
4. Recommandation Top-K

## Installation
// ```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
//

---

## 📁 `.venv/`

Environnement virtuel Python du projet.
Contient l’interpréteur Python et toutes les bibliothèques installées (torch, speechbrain, etc.).
Ne doit **jamais** être versionné sur GitHub.

---

## 📁 `data/`

Dossier contenant toutes les **données audio brutes**.
Inclut les musiques originales, les pistes vocales extraites et les enregistrements utilisateurs.
Exclu du dépôt Git pour des raisons de taille et de droits d’auteur.

---

## 📁 `embeddings/`

Stocke les **vecteurs d’embeddings vocaux** calculés pour chaque morceau.
Permet d’éviter de recalculer les embeddings à chaque exécution.
Non versionné car généré automatiquement.

---

## 📁 `metadata/`

Contient les **informations descriptives** des musiques (titre, artiste, identifiant, chemin).
Fait le lien entre les fichiers audio et leurs embeddings.
Peut être versionné car il ne contient pas d’audio.

---

## 📁 `src/`

Contient tout le **code source Python** du projet.
Chaque script correspond à une étape du pipeline (prétraitement, embedding, recommandation).
Structure pensée pour être modulaire et évolutive.

---

## 📄 `src/__init__.py`

Indique que `src` est un **module Python**.
Permet les imports propres entre fichiers du projet.
Ne contient généralement pas de logique métier.

---

## 📄 `src/audio_utils.py`

Fonctions utilitaires pour le **chargement et le prétraitement audio**.
Gère le passage en mono, le resampling et la normalisation.
Centralise les opérations audio communes au projet.

---

## 📄 `src/extract_vocals.py`

Script dédié à la **séparation de la voix** à partir des morceaux musicaux.
Utilise un modèle de séparation de sources (ex : Demucs).
Produit des fichiers `vocals.wav` exploitables pour l’analyse.

---

## 📄 `src/embed_catalog.py`

Calcule les **embeddings vocaux** des pistes voix du catalogue.
Utilise un réseau de neurones pré-entraîné (SpeechBrain / ECAPA).
Sauvegarde les vecteurs pour une utilisation ultérieure.

---

## 📄 `src/recommend.py`

Script principal de **recommandation musicale**.
Compare l’embedding de l’utilisateur à ceux du catalogue via similarité cosinus.
Retourne les musiques les plus proches vocalement.

---

## 📄 `.gitignore`

Liste les fichiers et dossiers à **exclure du versionnage Git**.
Empêche l’ajout des données, embeddings et du venv.
Indispensable pour un dépôt propre et léger.

---

## 📄 `README.md`

Document de présentation du projet.
Décrit l’objectif, l’architecture et les étapes principales du pipeline.
Point d’entrée pour toute personne consultant le dépôt GitHub.

---

## 📄 `requirements.txt`

Liste toutes les **dépendances Python** nécessaires au projet.
Permet de recréer exactement l’environnement via `pip install -r`.
Garantit la reproductibilité du projet.




sr veut dire sample rate (fréquence d’échantillonnage).

C’est le nombre de points par seconde utilisés pour représenter le son.

Exemples :

44100 Hz → 44 100 points par seconde (qualité CD)

22050 Hz → 22 050 points par seconde

16000 Hz → très courant en traitement vocal