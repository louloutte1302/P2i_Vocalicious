from navigate import *
from recommend import *
from navigate import clear
import warnings #ignorer les erreur librosa dans le terminal 

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

clear()

def main():
    user_folder = "data/vocals_to_analyse"
    
    # 1) choisir un fichier utilisateur via le terminal
    user_path = pick_file(user_folder)
    
    # 3) comparer et afficher résultats
    recommend(user_path)

    

if __name__ == "__main__":
    main()