"""
Loads the markdown corpus and produces text chunks.
"""

from pathlib import Path
import re

from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import (
    CORPUS_DIR,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


def clean_markdown(text: str) -> str:
    """
    Remove noisy markdown metadata before embedding.
    """

    text = re.sub(r"\*\*Source:.*", "", text)
    text = re.sub(r"\*\*Original URL:.*", "", text)
    text = re.sub(r"\*\*Document ID:.*", "", text)

    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def load_documents():
    """
    Read every markdown file from corpus/.
    """

    docs = []

    for path in sorted(Path(CORPUS_DIR).glob("*.md")):

        text = path.read_text(encoding="utf8")

        docs.append(
            {
                "doc_id": path.stem,
                "title": path.stem.replace("-", " ").title(),
                "text": clean_markdown(text),
            }
        )

    return docs


def chunk_documents(documents):
    """
    Split documents into recursive chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    chunks = []

    for doc in documents:

        pieces = splitter.split_text(doc["text"])

        for i, piece in enumerate(pieces):

            chunks.append(
                {
                    "chunk_id": f"{doc['doc_id']}_chunk_{i}",
                    "doc_id": doc["doc_id"],
                    "title": doc["title"],
                    "text": piece,
                }
            )

    return chunks


if __name__ == "__main__":

    docs = load_documents()

    print(f"Loaded {len(docs)} documents")

    chunks = chunk_documents(docs)

    print(f"Generated {len(chunks)} chunks")