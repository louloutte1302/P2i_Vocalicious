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


def calculation_pitch(y, sr):
    """
    Calcule le pitch (F0) avec librosa.pyin.
    Renvoie un tableau f0 (avec des NaN quand il n'y a pas de voix détectée).
    """
    f0,_,_ = librosa.pyin(y, fmin=fmin, fmax=fmax)

    # Suppr NaN
    f0_clean = []
    for value in f0:
        if not np.isnan(value):
            f0_clean.append(value)

    if len(f0_clean) == 0:
        return None  # pas de voix
    
    pitch_mean = sum(f0_clean) / len(f0_clean)

    return pitch_mean 





def compute_rms_mean(y):
    """
    Calcule l'énergie RMS moyenne (intensité moyenne).
    """
    rms_matrix = librosa.feature.rms(y=y)
    rms_mean = float(np.mean(rms_matrix)) #prsq rms renvoie un rms pour chaque frame découpé donc on prend une seule valeur moy 
    return rms_mean


