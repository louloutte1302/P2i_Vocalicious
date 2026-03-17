from pathlib import Path
import os

"""
Permet de proposer à l'utilisateur de jouer un extrait des musiques recommandées 
Récupère la sortie de recommend.py avec les noms des recommendations, les recroise 
avec les tracks initiaux de data/raw_traks. Utilise trim_to_30sec.py pour proposer 
les extraits des raw_tracks.

ATTENTION: ne fonctionne que sur macos! car utilise os

"""


def find_original_from_vocal(vocal_name, raw_folder="data/raw_tracks"):
    base_name = vocal_name.replace("-vocals", "")
    base_stem = Path(base_name).stem.lower()

    folder = Path(raw_folder)
    for f in folder.iterdir():
        if f.is_file() and f.stem.lower().endswith(base_stem):
            return f
        

    return None


def play_preview(vocal_name, start_sec=30, duration_sec=15):
    original_file = find_original_from_vocal(vocal_name, raw_folder="data/raw_tracks")

    if original_file is None:
        print("Morceau original introuvable.")
        return

    print(f"\nLecture de l'extrait : {vocal_name}")
    os.system(f'ffplay -nodisp -autoexit -ss {start_sec} -t {duration_sec} "{original_file}" >/dev/null 2>&1')