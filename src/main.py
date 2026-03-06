from .recommend import *

def main():
    user_folder = "data/vocals_to_analyse"
    
    # 1) choisir un fichier utilisateur via le terminal
    user_path = pick_file(user_folder)

    # 2) extraire features utilisateur
    extract_voice_features(str(user_path))
    
    # 4) comparer et afficher résultats
    recommend(user_path)

    

if __name__ == "__main__":
    main()