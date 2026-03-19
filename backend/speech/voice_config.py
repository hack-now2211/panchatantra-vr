import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# safer indexing (important)
character_voices = {
    "lion": voices[0].id,
    "rabbit": voices[1].id if len(voices) > 1 else voices[0].id,
    "animals": voices[1].id if len(voices) > 1 else voices[0].id,
    "narrator": voices[0].id
}

def get_voice(character):
    return character_voices.get(character, voices[0].id)