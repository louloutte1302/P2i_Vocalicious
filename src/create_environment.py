"""
À lancer dès le téléchargement initial, si vous souhaitez travailler sur votre 
propre base de données de musiques

1- Demande si vous voulez travailler avec la base de données disponible ou la vôtre
    - si celle disponible = passer les étapes d'après
    - si leur propre BDD = importer leur base de données qui remplace celles dans raw_tracks
2- Vérifie les doublons via delete_duplicates.py
3- Extrait les vocals via extract_vocals.py
4- Coupe les vocals à 30sec via trim_to_30sec.py
5- Coupe les raws_track à 30 sec (ou pas à voir) via trim_to_30sec.py
6- Renomme les tracks de façon correcte et les mets dans leur bon dossier via collect_vocals.py
7- Créer le catalog des vocals

"""

def create_environment():
    {
    }