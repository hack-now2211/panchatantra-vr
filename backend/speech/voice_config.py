import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

# Map characters to voices
character_voices = {
    "lion": voices[0].id,     # deep voice
    "rabbit": voices[1].id,   # lighter voice
    "animals": voices[1].id
}

def get_voice(character):
    return character_voices.get(character, voices[0].id)