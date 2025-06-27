# vector_store.py
import faiss
import numpy as np

def create_faiss_index(embeddings):
    """
    Creates a FAISS index from embeddings.
    """
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension) # L2 distance for similarity
    index.add(embeddings)
    print(f"FAISS index created with {index.ntotal} vectors.")
    return index

def search_faiss_index(index, query_embedding, k=3):
    """
    Searches the FAISS index for the top-k most similar embeddings.
    """
    distances, indices = index.search(np.array([query_embedding]), k)
    print(f"Found top {k} similar vectors.")
    return distances, indices

if __name__ == "__main__":
    # Example usage:
    # Assuming you have sample_embeddings from embeddings_generator.py
    # (or load from a saved .npy file)
    # For demonstration, let's generate some dummy embeddings
    dummy_embeddings = np.random.rand(100, 384).astype('float32') # 100 vectors, 384 dim (MiniLM output)
    
    index = create_faiss_index(dummy_embeddings)
    
    # Simulate a query embedding
    dummy_query_embedding = np.random.rand(384).astype('float32')
    
    distances, indices = search_faiss_index(index, dummy_query_embedding, k=5)
    print("Distances:", distances)
    print("Indices (of original texts):", indices)
    
    # Save/Load index (useful for persistence)
    faiss.write_index(index, "my_document_index.faiss")
    loaded_index = faiss.read_index("my_document_index.faiss")
    print(f"Loaded index has {loaded_index.ntotal} vectors.")