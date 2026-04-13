import sounddevice as sd
from scipy.io.wavfile import write
from pathlib import Path
import time

"""
record_audio.py

Enregistre un audio via le micro du matériel utilisé
puis enregistre l'audio dans le dossier vocals_to_analyse

"""

def record_audio ():
    fs = 44100  # fréquence d'échantillonnage
    duration = 27  # secondes

    folder = Path("data/vocals_to_analyse")
    file_path = folder/"mon-enregistrement.wav"

    print("L'enregistrement va se lancer dans 5 secondes, faites des vocalises pdt 30 sec")
    time.sleep(5)

    print("Enregistrement...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print("Enregistrement terminé.")

    write(file_path, fs, audio)
    print("Enregistrement sauvegardé avec succès !")

    return(file_path)
