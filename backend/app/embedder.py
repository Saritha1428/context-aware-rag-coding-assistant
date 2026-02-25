import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load the model globally for better performance
model = SentenceTransformer('all-MiniLM-L6-v2')

def process_and_store_embeddings(chunks):
    if not chunks:
        return None
    
    # 1. Convert text to numerical vectors
    texts = [chunk['text'] for chunk in chunks]
    embeddings = model.encode(texts)
    embeddings = np.array(embeddings).astype('float32')
    
    # 2. Initialize FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    
    # 3. Save the index locally for retrieval
    faiss.write_index(index, "vector_store.bin")
    
    return {"status": "success", "indexed_chunks": len(chunks)}