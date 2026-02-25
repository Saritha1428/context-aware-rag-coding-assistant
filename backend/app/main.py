from fastapi import FastAPI
from .code_loader import load_project_files
from .chunker import chunk_code 
from .embedder import process_and_store_embeddings
from .retriever import retrieve_context
from .rag_engine import generate_answer

app = FastAPI(title="CTRL ALT WIN - AI Backend")

# Global variable to hold chunks temporarily
stored_chunks = []

@app.get("/process")
def process_project(path: str):
    global stored_chunks
    raw_files = load_project_files(path)
    stored_chunks = chunk_code(raw_files)
    indexing_result = process_and_store_embeddings(stored_chunks)
    
    return {
        "status": "success",
        "files_found": len(raw_files),
        "indexing": indexing_result
    }

@app.get("/ask")
def ask_question(query: str):
    if not stored_chunks:
        return {"error": "Please run /process first."}
    
    # 1. Relevant code snippets ni vethukuthundi
    context_chunks = retrieve_context(query, stored_chunks)
    
    # 2. OpenAI ni vaadi answer generate chestundi
    answer = generate_answer(query, context_chunks)
    
    return {
        "query": query,
        "answer": answer,
        "source_files": list(set([c['file_name'] for c in context_chunks]))
    }