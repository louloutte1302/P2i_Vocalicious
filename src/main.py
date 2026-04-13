#from create_environment import *
from navigate import pick_file, clear, pick_from_list, pick_audio
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

    # 2) Choisir si l'on enregistre ou l'on importe un audio
    user_path= pick_audio("data/vocals_to_analyse")
    
    # 3) comparer et afficher résultats
    recommended_tracks=recommend(user_path)
    
    # 4) choisir un fichier utilisateur via le terminal
    while True:
        selected_track = pick_from_list(recommended_tracks)

        if selected_track is None:
            print("Merci d'avoir utilisé cette appli")
            break

    # 5) Jouer les extraits des musiques
        play_preview(selected_track)



if __name__ == "__main__":
    main()