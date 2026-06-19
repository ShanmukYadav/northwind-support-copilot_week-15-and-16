"""
LLM generation using Groq.
"""

import os

from dotenv import load_dotenv
from groq import Groq

from app.config import LLM_MODEL

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError(
        "GROQ_API_KEY not found in .env"
    )

client = Groq(api_key=api_key)


def generate_answer(system_prompt: str, user_prompt: str) -> str:
    """
    Generate an answer using Groq.
    """

    response = client.chat.completions.create(
        model=LLM_MODEL,
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    answer = generate_answer(
        "You are helpful.",
        "Say hello."
    )

    print(answer)