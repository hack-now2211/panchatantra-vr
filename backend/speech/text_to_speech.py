from gtts import gTTS
import os
import tempfile
import threading
from playsound import playsound

lock = threading.Lock()


def speak(text, character):

    with lock:  # prevents overlapping audio

        print(f"\n🔊 {character} speaking...")

        try:
            # 🔥 Create TTS
            tts = gTTS(text=text, lang='en')

            # 🔥 Save to temp file
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            temp_path = temp_file.name
            temp_file.close()

            tts.save(temp_path)

            # 🔥 Play audio
            playsound(temp_path)

            # 🔥 Delete file after playing
            os.remove(temp_path)

        except Exception as e:
            print("TTS Error:", e)