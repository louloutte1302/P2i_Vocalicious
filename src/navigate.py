from pathlib import Path


def pick_file(folder_path):
    folder = Path(folder_path)

    files = [f for f in folder.iterdir() if f.is_file()]
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