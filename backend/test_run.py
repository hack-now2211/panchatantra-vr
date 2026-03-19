from backend.scene_engine.scene_manager import SceneManager
from backend.ai_dialogue.character_ai import generate_character_reply
from backend.speech.speech_to_text import listen
from backend.speech.text_to_speech import speak
import time
manager = SceneManager()

while True:

    scene = manager.get_scene()

    print("\n--- Scene ---")
    print("Narration:", scene["narration"])

    # 🔊 Narration (always spoken)
    speak(scene["narration"], "narrator")
    time.sleep(1)  # 🔥 prevents audio drop
    # 🔊 Dialogues
    for d in scene["dialogues"]:
        print(f"{d['character']}: {d['text']}")
        speak(d["text"], d["character"])
        time.sleep(0.4)  # 🔥 prevents audio drop

    # 🎤 Interaction loop
    while True:

        print("\n🎤 Speak (say 'next' to continue)...")

        user_input = listen()

        if user_input == "":
            continue

        if "next" in user_input:
            break

        reply = generate_character_reply(
            scene["active_character"],
            user_input,
            scene
        )

        print(f"{scene['active_character']}:", reply)

        # 🔊 Reply voice
        speak(reply, scene["active_character"])

    manager.next_scene()