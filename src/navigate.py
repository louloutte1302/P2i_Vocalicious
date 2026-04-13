from pathlib import Path
import record_audio


def pick_file(folder_path):

    """
    Permet à l'utilisateur de sélectionner un fichier dans un dossier
    via une interface console.

    La fonction liste tous les fichiers présents dans le dossier des audios utilisateur,
    les affiche avec un numéro associé, puis demande à l'utilisateur d'entrer le numéro correspondant au fichier qu'il souhaite utiliser.

    La fonction continue de demander une entrée tant qu'un numéro valide
    correspondant à un fichier existant n'est pas fourni.
    """

    folder = Path(folder_path)

    # print("Dossier lu :", folder.resolve())

    all_files = [f for f in folder.iterdir() if f.is_file()]
    # print("Tous les fichiers :", [f.name for f in all_files])
    
    files = [
    f for f in all_files
        if not f.name.startswith(".")
        and f.name.lower().endswith((".m4a", ".wav", ".mp3"))
]
    files.sort()

    if len(files) == 0:
        raise ValueError("Aucun fichier trouvé.")

    print("\nChoisis un fichier :\n")

    for i, f in enumerate(files):
        print(f"{i + 1} - {f.name}")

    while True:
        choice = input("\nNuméro du fichier : ")

        if choice.isdigit():
            index = int(choice) - 1

            if 0 <= index < len(files):
                return files[index]

        print("Choix invalide, recommencez.")


def pick_from_list(items):
    """
    Permet de sélectionner un élément dans une liste via le terminal.
    """
    if len(items) == 0:
        return("Liste vide.")


    print("\nChoisis un morceau de 1 à 5 à écouter (0 - Quitter):\n")

    choice = input("\nNuméro du morceau : ")
    
    if choice.isdigit():
        index = int(choice)

        if 1 <= index <= len(items):
            return items[index - 1]

        else: return None
        
def clear():
    print("\033c", end="")

def pick_audio(folder_path):
    """
    Permet de choisir entre importer un audio ou en enregistrer un.
    """

    while True:
        print("\nQue veux-tu faire ?\n")
        print("1 - Importer un audio existant")
        print("2 - Enregistrer un audio avec le micro")

        choice = input("\nTon choix : ")

        if choice == "1":
            return pick_file(folder_path)

        elif choice == "2":
            return record_audio.record_audio()

        else:
            print("Choix invalide, recommence.")