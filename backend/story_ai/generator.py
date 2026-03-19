import logging
import time
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# ------------------------------------
# Logger
# ------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# ------------------------------------
# Load Model
# ------------------------------------
logger.info("Loading AI model...")

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

start_load = time.time()

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

end_load = time.time()

logger.info(f"Model loaded successfully in {end_load-start_load:.2f} seconds")

# ------------------------------------
# Story Generator
# ------------------------------------
def generate_story():

    prompt = """
You are a storyteller.

Write a Panchatantra style story.

Requirements:
- Start with "Once upon a time in a forest"
- Characters: a clever fox and a crow
- The fox flatters the crow to steal cheese
- The crow sings proudly and drops the cheese
- The fox runs away with the cheese
- End with "Moral:" and a lesson

Story length: about 300–400 words.
"""

    logger.info("Generating story...")

    start_gen = time.time()

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=500,
        temperature=0.8,
        top_p=0.9,
        repetition_penalty=1.2,
        do_sample=True
    )

    story = tokenizer.decode(outputs[0], skip_special_tokens=True)

    end_gen = time.time()

    logger.info(f"Story generated in {end_gen-start_gen:.2f} seconds")

    return story

# ------------------------------------
# Main
# ------------------------------------
if __name__ == "__main__":

    total_start = time.time()

    story = generate_story()

    print("\nGenerated Story:\n")
    print(story)

    total_end = time.time()

    logger.info(f"Total execution time: {total_end-total_start:.2f} seconds")