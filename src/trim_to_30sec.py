"""
trim_to_30s.py

Crée des extraits de 30 secondes maximum pour tous les fichiers audio
du dossier `data/vocals_only`.

Les fichiers courts (<30s) sont laissés tels quels.
Les extraits sont sauvegardés dans `data/vocals_30s`.
"""

import librosa
import soundfile as sf
from pathlib import Path
from tqdm import tqdm

INPUT_FOLDER = Path("data/vocals_only")
OUTPUT_FOLDER = Path("data/vocals_30sec")

OUTPUT_FOLDER.mkdir(exist_ok=True)

MAX_DURATION = 30  # secondes

files = [f for f in INPUT_FOLDER.iterdir() if f.is_file()]

for f in tqdm(files, desc="Découpage des audios"):
    
    # charger audio
    y, sr = librosa.load(f, sr=None)

    max_samples = sr * MAX_DURATION
    y_trim = y[:max_samples]

    output_path = OUTPUT_FOLDER / f.name

    # sauvegarder
    sf.write(output_path, y_trim, sr)

print("\nExtraits de 30s créés dans :", OUTPUT_FOLDER)