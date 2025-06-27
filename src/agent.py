# agent.py
from src.document_processor import extract_text_from_pdf
from src.embeddings_generator import create_embeddings
from src.vector_store import create_faiss_index, search_faiss_index
from langchain_community.llms import Ollama # For interacting with local Ollama LLM
import os # For checking file existence

# Global variables for the agent (loaded once)
document_texts = []
document_embeddings = None
faiss_index = None
llm = None

def initialize_agent(pdf_path, llm_model_name="llama3"):
    """
    Initializes the AI agent by processing the document and setting up the LLM.
    """
    global document_texts, document_embeddings, faiss_index, llm

    print(f"Initializing agent with document: {pdf_path}")
    
    # 1. Extract text
    document_texts = extract_text_from_pdf(pdf_path)
    if not document_texts:
        raise ValueError("No text extracted from the document. Please check the PDF path and content.")

    # 2. Create embeddings
    document_embeddings = create_embeddings(document_texts).astype('float32')

    # 3. Create FAISS index
    faiss_index = create_faiss_index(document_embeddings)
    
    # 4. Initialize LLM
    try:
        llm = Ollama(model=llm_model_name, temperature=0.1) # Lower temperature for factual answers
        print(f"Ollama LLM '{llm_model_name}' initialized.")
    except Exception as e:
        print(f"Could not connect to Ollama or load model '{llm_model_name}'. Make sure Ollama is running and the model is downloaded.")
        print(f"Error: {e}")
        llm = None # Set to None to handle gracefully

def query_agent(query):
    """
    Queries the agent about the document content using RAG.
    """
    if llm is None or faiss_index is None or document_texts is None:
        return "Agent not initialized. Please run initialize_agent() first and ensure Ollama is running."

    print(f"\nUser Query: {query}")

    # 1. Create embedding for the query (initialize model if needed)
    from src.embeddings_generator import create_embeddings
    query_embedding = create_embeddings([query]).astype('float32')[0]

    # 2. Search for relevant document chunks
    distances, indices = search_faiss_index(faiss_index, query_embedding, k=2) # Get top 2 relevant chunks

    relevant_chunks = []
    for idx in indices[0]:
        if idx < len(document_texts): # Ensure index is valid
            relevant_chunks.append(document_texts[idx])

    if not relevant_chunks:
        return "Could not find relevant information in the document."

    # 3. Construct prompt for LLM
    context = "\n\n".join(relevant_chunks)
    
    # Basic prompt template using f-strings
    # You can also use LangChain's PromptTemplate for more advanced prompting
    prompt_template = f"""
    You are an intelligent assistant that answers questions based *only* on the provided document context.
    If the answer is not available in the context, state that you cannot find the information in the document.

    Document Context:
    {context}

    Question: {query}

    Answer:
    """

    print("\n--- Sending to LLM with context ---")
    # 4. Get answer from LLM
    try:
        response = llm.invoke(prompt_template)
        print("--- LLM Response Received ---")
        return response.strip()
    except Exception as e:
        return f"Error getting response from LLM: {e}. Make sure Ollama is running and accessible."

if __name__ == "__main__":
    # Ensure you have 'sample.pdf' in your project directory
    sample_pdf_path = "sample.pdf"
    
    if not os.path.exists(sample_pdf_path):
        print(f"Error: '{sample_pdf_path}' not found. Please create a dummy PDF or replace with your actual document path.")
        print("Instructions for dummy PDF: Create a text file, add some content, save as .txt, then print to PDF from your text editor.")
    else:
        initialize_agent(sample_pdf_path)

        if llm: # Only proceed if LLM was initialized successfully
            while True:
                user_question = input("\nAsk a question about the document (type 'exit' to quit): ")
                if user_question.lower() == 'exit':
                    break
                answer = query_agent(user_question)
                print(f"\nAgent: {answer}")
        else:
            print("Agent could not be fully initialized due to LLM issues. Exiting.")