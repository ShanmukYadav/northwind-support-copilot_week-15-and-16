"""
Application configuration for Northwind Support Copilot.
Centralizes all configurable parameters.
"""

from pathlib import Path

# ------------------------------------------------------------------
# Project Paths & Database
# ------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CORPUS_DIR = PROJECT_ROOT / "corpus"

CHROMA_DIR = PROJECT_ROOT / "app" / ".chroma_db"

COLLECTION = "northwind_rag"

# ------------------------------------------------------------------
# Embedding Model
# ------------------------------------------------------------------

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ------------------------------------------------------------------
# Chunking
# ------------------------------------------------------------------

CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

# ------------------------------------------------------------------
# Retrieval
# ------------------------------------------------------------------

TOP_K = 6

MAX_CHUNKS_PER_DOC = 15

# ------------------------------------------------------------------
# LLM
# ------------------------------------------------------------------
LLM_MODEL = "llama-3.3-70b-versatile"
# Environment Variable
# set GROQ_API_KEY=<your_key>

# ------------------------------------------------------------------
# Evaluation
# ------------------------------------------------------------------

GOLDEN_SET_PATH = PROJECT_ROOT / "eval" / "golden_questions.json"

# ------------------------------------------------------------------
# Misc
# ------------------------------------------------------------------

RANDOM_SEED = 42