import numpy as np
import librosa


def load_audio(audio_path, target_sr):

    """
    Charge un fichier audio en mono et le met au sample rate target_sr.
    Renvoie : y (signal), sr (sample rate)
    """

    y, sr = librosa.load(audio_path, sr=target_sr, mono=True)
    # remet au niveau sample rate nécessaire (inf à 8hz pour les humains donc env 22000 c'est top) audio nécessaire 
    # + en mono et non stéréo (une seule sortie et non droite gauche)

    if len(y) == 0:
        raise ValueError("Audio vide ou illisible.")

    return y, sr

