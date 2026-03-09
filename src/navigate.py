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
    files = [
    f for f in folder.iterdir()
    if f.is_file() and f.suffix.lower() in [".m4a", ".wav", ".mp3"]
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

        print("Choix invalide, recommence.")

def clear():
    print("\033c", end="")