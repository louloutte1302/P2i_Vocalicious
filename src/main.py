#from create_environment import *
from navigate import pick_file, clear, pick_from_list
from recommend import recommend
from play_track import play_preview
import warnings
from create_environment import check_dataset


warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

clear()

def main():
    # 1) définir le dataset
    check_dataset()

    
    # 2) choisir un fichier utilisateur via le terminal
    user_path = pick_file("data/vocals_to_analyse")
    
    # 3) comparer et afficher résultats
    recommended_tracks=recommend(user_path)

    # 4) choisir un fichier utilisateur via le terminal
    selected_track = pick_from_list(recommended_tracks)

    # 5) Jouer les extraits des musiques
    play_preview(selected_track)


if __name__ == "__main__":
    main()