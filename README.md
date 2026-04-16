## Vocalicious

Vocalicious est une application qui recommande des musiques à partir de la voix chantée de l’utilisateur.
L’utilisateur peut importer ou enregistrer un extrait vocal, qui est ensuite analysé pour proposer des morceaux ayant des caractéristiques vocales similaires.

---

Auteur: Lou Pépin Poussard - Groupe 3 - 2A - Promotion 2027

Projet réalisé dans le cadre du P2I — ENSC Bordeaux INP

---

## Fonctionnalités

* Import d’un fichier audio (.wav, .mp3, .m4a)
* Enregistrement d’un audio via le micro
* Analyse vocale (pitch, énergie, timbre)
* Recommandation des 5 morceaux les plus similaires
* Lecture des extraits recommandés
* Interface web simple (Flask)

---

## Méthode

L’application repose sur une approche en **machine learning classique** :

### Extraction des features vocales

* Pitch (hauteur)
* RMS (énergie)
* MFCC (timbre)

### Représentation

→ vecteur de caractéristiques pour chaque audio

### Comparaison

* Normalisation (`StandardScaler`)
* Similarité cosinus

### Résultat

→ Top 5 des morceaux les plus proches

---

## Architecture
```text

P2i/
├── app.py                 # Application Flask
├── src/                   # Logique métier
│   ├── recommend.py
│   ├── extract_feat_vocals.py
│   ├── record_audio.py
│   ├── play_track.py
│   └── ...
├── templates/
│   └── index.html         # Interface web
├── static/
│   └── style.css          # Design
├── data/
│   ├── raw_tracks/        # Musiques originales
│   ├── vocals_only/       # Voix extraites
│   ├── vocals_30sec/      # Extraits courts
│   ├── catalog.npy        # Features
│   └── vocals_to_analyse/ # Dossiers des audios à analyser
```

---

## Installation

### 1. Cloner le projet

```bash
git clone <https://github.com/louloutte1302/P2i_Vocalicious.git>
```

---

### 2. Créer un environnement virtuel

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

(ou manuellement : librosa, numpy, sklearn, flask, sounddevice, scipy)

---

# Lancer l’application sur navigateur
  1. Se placer sur la branche interface
```bash
git checkout interface
```
   2. Lancer l'app
```bash
python app.py
```

  3. Ouvrir dans le navigateur
```text
http://127.0.0.1:5055
```
Si une erreur 403, 404 ou tout autre problème survient: relancer le code et retenter
---
# Lancer la version console

  1. Se placer sur la branche console
```bash
git checkout console
```

2. Lancer le programme
```bash
python src/main.py
```


