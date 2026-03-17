from create_environment import *
from navigate import *
from recommend import *
from navigate import clear
from play_track import *
import warnings

from src import create_environment #ignorer les erreur librosa dans le terminal 

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

clear()

def main():
    # 1) définir le dataset
    #create_environment()

    user_folder1 = "data/vocals_to_analyse"
    user_folder2 = "data/raw_track"
    
    # 1) choisir un fichier utilisateur via le terminal
    user_path = pick_file(user_folder1)
    
    # 2) comparer et afficher résultats
    recommend(user_path)

    # 3) choisir un fichier utilisateur via le terminal
    user_path = pick_file(user_folder2)

    # 4) Jouer les extraits des musiques
    play_track(user_path)

    

if __name__ == "__main__":
    main()