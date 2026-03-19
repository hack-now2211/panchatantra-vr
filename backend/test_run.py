from backend.scene_engine.scene_manager import SceneManager
from backend.ai_dialogue.character_ai import generate_character_reply

manager = SceneManager()

while True:

    scene = manager.get_scene()

    print("\n--- Scene ---")
    print("Narration:", scene["narration"])

    for d in scene["dialogues"]:
        print(f"{d['character']}: {d['text']}")

    # 🔁 MULTI-TURN INTERACTION
    while True:
        user_input = input("\nYou (type 'next' to continue): ")

        if user_input.lower() == "next":
            break

        reply = generate_character_reply(
            scene["active_character"],
            user_input,
            scene
        )

        print(f"{scene['active_character']}:", reply)

    manager.next_scene()