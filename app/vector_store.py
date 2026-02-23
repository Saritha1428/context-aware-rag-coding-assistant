# backend/app/vector_store.py
import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimension=384): # all-MiniLM-L6-v2 dimension 384
        self.index = faiss.IndexFlatL2(dimension)
        self.metadata = []

    def add_to_index(self, chunks, embeddings):
        embeddings_np = np.array(embeddings).astype('float32')
        self.index.add(embeddings_np)
        # Store metadata (file name and text) to retrieve later
        for chunk in chunks:
            self.metadata.append({
                "file_name": chunk['file_name'],
                "text": chunk['text']
            })

    def search(self, query_embedding, k=3):
        query_np = np.array([query_embedding]).astype('float32')
        distances, indices = self.index.search(query_np, k)
        
        results = []
        for i in indices[0]:
            if i != -1: # Valid index check
                results.append(self.metadata[i])
        return results

# Shared instance
vector_db = VectorStore()