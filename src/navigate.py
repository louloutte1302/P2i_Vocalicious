from pathlib import Path


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

    print("\nChoisis un morceau à écouter (0 - Quitter):\n")

    
    while True:
        choice = input("\nNuméro du morceau : ")

        if choice.isdigit():
            index = int(choice)

            if index == 0:
                return None

            if 1 <= index <= len(items):
                return items[index - 1]

        print("Choix invalide, recommence.")

def clear():
    print("\033c", end="")