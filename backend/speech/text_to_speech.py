import pyttsx3
from backend.speech.voice_config import get_voice

engine = pyttsx3.init()

def speak(text, character):

    voice_id = get_voice(character)

    engine.setProperty('voice', voice_id)
    engine.setProperty('rate', 170)

    print(f"\n🔊 {character} speaking...")

    engine.say(text)
    engine.runAndWait()