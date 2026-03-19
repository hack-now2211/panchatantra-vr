import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import tempfile

def listen():

    duration = 5  # seconds
    sample_rate = 16000

    print("\n🎤 Listening... Speak now")

    recording = sd.rec(int(duration * sample_rate),
                       samplerate=sample_rate,
                       channels=1,
                       dtype='int16')

    sd.wait()

    # Save to temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    wav.write(temp_file.name, sample_rate, recording)

    recognizer = sr.Recognizer()

    with sr.AudioFile(temp_file.name) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You (voice):", text)
        return text.lower()

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return ""

    except sr.RequestError:
        print("❌ API unavailable")
        return ""