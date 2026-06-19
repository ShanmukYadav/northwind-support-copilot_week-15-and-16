"""
End-to-end Retrieval Augmented Generation pipeline.
"""

from app.retrieve import build_index, retrieve
from app.prompt import build_prompt
from app.generate import generate_answer


class RAGPipeline:
    """
    Northwind Support Copilot RAG Pipeline.
    """

    def __init__(self):

        print("Loading retrieval index...\n")

        self.collection, self.model = build_index()

        print("Ready.\n")

    def ask(self, question: str) -> dict:
        """
        Ask a question to the RAG system.
        """

        retrieved = retrieve(
            question,
            self.collection,
            self.model,
        )
        print("\nRetrieved Documents:")
        for chunk in retrieved:
            print(f"{chunk['doc_id']}  score={chunk['score']}")

        system_prompt, user_prompt = build_prompt(
            question,
            retrieved,
        )

        answer = generate_answer(
            system_prompt,
            user_prompt,
        )

        sources = []

        seen = set()

        for chunk in retrieved:

            if chunk["title"] not in seen:

                seen.add(chunk["title"])

                sources.append(chunk["title"])

        return {
            "question": question,
            "answer": answer,
            "sources": sources,
            "retrieved_chunks": retrieved,
        }


if __name__ == "__main__":

    rag = RAGPipeline()

    while True:

        print()

        question = input("Ask a question (or type exit): ")

        if question.lower() == "exit":
            break

        result = rag.ask(question)

        print("\n" + "=" * 80)
        print("ANSWER\n")
        print(result["answer"])

        print("\nSOURCES")

        for source in result["sources"]:
            print(f"- {source}")

        print("=" * 80)