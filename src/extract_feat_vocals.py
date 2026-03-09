import numpy as np
import librosa
from navigate import clear


def load_audio(audio_path, target_sr):
    """
    Charge un fichier audio en mono et le met au sample rate target_sr.
    Renvoie : y (signal), sr (sample rate)
    """
    y, sr = librosa.load(audio_path, sr=target_sr, mono=True)
    # fichier vide
    if len(y) == 0:
        raise ValueError("Audio vide ou illisible.")
    
    # fichier silencieux (toutes les amplitudes ~0)
    rms = np.sqrt(np.mean(y ** 2))
    if rms < 1e-3:
        raise ValueError("Audio silencieux.")

    return y, sr


def compute_pitch(y, sr):
    """
    Calcule le pitch (F0) avec librosa.pyin.
    Renvoie un tableau f0 (avec des NaN quand il n'y a pas de voix détectée).
    """
    fmin = float(librosa.note_to_hz("C2")) #note la plus basse jamais chantée par un homme
    fmax = float(librosa.note_to_hz("C7")) #note la plus haute jamais chantée par une femme
  

    f0, _, _ = librosa.pyin(y, fmin=fmin, fmax=fmax)

    # Suppr NaN
    f0_clean = []
    for value in f0:
        if not np.isnan(value):
            f0_clean.append(value)

    if len(f0_clean) == 0:
        return None  # pas de voix
    
    pitch_mean = sum(f0_clean) / len(f0_clean)

    return pitch_mean 



def pitch_to_category(pitch_mean_hz):
    """
    Associe un pitch moyen (en Hz) à une tessiture approximative.
    """

    if pitch_mean_hz is None:
        return "inconnu"

    # Voix masculines 
    if 82 <= pitch_mean_hz < 110:
        return "Basse"

    elif 110 <= pitch_mean_hz < 130:
        return "Baryton"

    elif 130 <= pitch_mean_hz < 175:
        return "Ténor"

    # Voix féminines 
    elif 175 <= pitch_mean_hz < 220:
        return "Alto (Contralto)"

    elif 220 <= pitch_mean_hz < 261:
        return "Mezzo-soprano"

    elif 261 <= pitch_mean_hz <= 1046:
        return "Soprano"

    else:
        return "Hors plage vocale standard"



def compute_rms_mean(y):
    """
    Calcule l'énergie RMS moyenne (intensité moyenne).
    """
    rms_matrix = librosa.feature.rms(y=y)
    rms_mean = float(np.mean(rms_matrix))
    return rms_mean


def compute_mfcc_means(y, sr, n_mfcc):

    """
    Permet de récupérer le timbre, la couleur de la voix
    Calcule les MFCC, puis renvoie la moyenne de chaque coefficient MFCC. 
    """

    mfcc_matrix = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)

    # moyenne sur le temps (axis=1 car shape = (n_mfcc, frames))
    mfcc_means = np.mean(mfcc_matrix, axis=1)

    return mfcc_means.astype(np.float32)


def extract_voice_features(audio_path, target_sr=22050, n_mfcc=13):
    """
    Converti toutes les données précédentes en un seul vecteur
    """
    clear()
    print("\n==============================")
    print("\nAnalyse audio en cours...")
    print("\n==============================")
   
    # charger audio
    try:
        y, sr = load_audio(audio_path, target_sr)
    except ValueError as e:
        print(f"⚠️ {e}")
        return None, "inconnu"


    # pitch
    pitch_mean = compute_pitch(y, sr)
    pitch_label = pitch_to_category(pitch_mean)

    # si pas de pitch détecté, on ignore le fichier
    if pitch_mean is None:
        return None, pitch_label

    # rms
    rms_mean = compute_rms_mean(y)

    # mfcc
    mfcc_means = compute_mfcc_means(y, sr, n_mfcc)

    # vecteur numérique final
    # -> 1 pitch + 1 rms + 13 mfcc = 15 valeurs
    if pitch_mean != None:
        features = np.concatenate([np.array([pitch_mean, rms_mean], dtype=np.float32), mfcc_means])
        return features, pitch_label
    else:
        features = None
        return features, pitch_label