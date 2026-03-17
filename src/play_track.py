from pathlib import Path


"""
Permet de proposer à l'utilisateur de jouer un extrait des musiques recommandées 
Récupère la sortie de recommend.py avec les noms des recommendations, les recroise 
avec les tracks initiaux de data/raw_traks. Utilise trim_to_30sec.py pour proposer 
les extraits des raw_tracks.

ATTENTION: ne fonctionne que sur macos! car utilise os

"""

def play_track(track_to_play):
    { }