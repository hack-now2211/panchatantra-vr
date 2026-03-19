from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_character_reply(character, user_input, scene):

    dialogue_text = "\n".join(
        [f"{d['character']}: {d['text']}" for d in scene['dialogues']]
    )

    prompt = f"""
You are {character} from the story "Lion and the Clever Rabbit".

SCENE:
{scene['narration']}

DIALOGUE:
{dialogue_text}

STRICT RULES:
- Speak ONLY as {character}
- Stay ONLY in this scene
- Do NOT mention future events
- Do NOT invent new story
- Reply in 1 short sentence (max 12 words)
- Be natural and simple

User: {user_input}
{character}:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a character inside a fixed story. Never go outside the given scene."
            },
            {"role": "user", "content": prompt}
        ],
        max_tokens=50,
        temperature=0.5
    )

    return response.choices[0].message.content.strip()