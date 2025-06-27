# embeddings_generator.py
from sentence_transformers import SentenceTransformer

def create_embeddings(texts):
    """
    Creates embeddings for a list of text strings using a pre-trained model.
    """

    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("Loading Sentence Transformer model...")
    embeddings = model.encode(texts, show_progress_bar=True)
    print(f"Created {len(embeddings)} embeddings.")
    return embeddings

if __name__ == "__main__":
    # Example usage:
    sample_texts = [
        "The quick brown fox jumps over the lazy dog.",
        "A red fox quickly leaps over a sleepy canine.",
        "Artificial intelligence is transforming industries.",
        "Machine learning is a subset of AI."
    ]
    sample_embeddings = create_embeddings(sample_texts)
    print(f"Shape of embeddings: {sample_embeddings.shape}")