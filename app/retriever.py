import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def retrieve_context(query, chunks, top_k=2):
    # Read the stored database
    index = faiss.read_index("vector_store.bin")
    
    # Convert query to vector
    query_vector = model.encode([query]).astype('float32')
    
    # Search for top relevant snippets
    distances, indices = index.search(query_vector, top_k)
    
    relevant_chunks = [chunks[i] for i in indices[0]]
    return relevant_chunks