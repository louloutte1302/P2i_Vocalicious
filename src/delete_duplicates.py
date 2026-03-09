from pathlib import Path
"""
delete_duplicate.py

Supprime automatiquement les fichiers audio en doublon dans le dossier
`data/vocals_only`.

Un doublon est ici défini comme un fichier dont le nom contient un suffixe
de copie automatique, par exemple :
- nom-2.mp4
- nom-3.m4a
...
"""
folder = Path("data/vocals_only")

deleted = 0

for f in folder.iterdir():
    if f.is_file() and "-2." in f.name:
        print("Suppression :", f.name)
        f.unlink()
        deleted += 1

print("\nTotal supprimés :", deleted)