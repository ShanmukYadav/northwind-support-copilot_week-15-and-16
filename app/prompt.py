"""
Prompt builder for the Northwind Support Copilot.
Creates the final prompt sent to the LLM.
"""

SYSTEM_PROMPT = """
You are Northwind Support Copilot.

Answer ONLY using the provided documentation context.

Rules:

1. If the answer exists in the context, answer clearly.

2. If the answer cannot be found in the context,
reply exactly:

I do not know based on the provided documentation.

3. Never invent information.

4. Always include the document titles used as sources.

5. Keep answers concise and factual.
""".strip()


def build_prompt(question: str, retrieved_chunks: list[dict]) -> tuple[str, str]:
    """
    Build the system prompt and user prompt.

    Returns:
        (system_prompt, user_prompt)
    """

    context_blocks = []

    for i, chunk in enumerate(retrieved_chunks, start=1):

        context_blocks.append(
            f"""
Document {i}

Title:
{chunk['title']}

Content:
{chunk['text']}
""".strip()
        )

    context = "\n\n-----------------------------\n\n".join(context_blocks)

    user_prompt = f"""
Context

{context}

====================================

Question

{question}

Answer using ONLY the context above.

At the end include:

Sources:
- document title(s)
""".strip()

    return SYSTEM_PROMPT, user_prompt


if __name__ == "__main__":

    sample = [
        {
            "title": "Projects",
            "text": "Projects help organize work across multiple teams."
        }
    ]

    system, user = build_prompt(
        "What are projects?",
        sample
    )

    print("SYSTEM PROMPT\n")
    print(system)

    print("\n\nUSER PROMPT\n")
    print(user)