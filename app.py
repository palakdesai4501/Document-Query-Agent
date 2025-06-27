# app.py
import streamlit as st
from src.agent import initialize_agent, query_agent, llm # Import shared components and LLM status
import os

# Streamlit page configuration
st.set_page_config(page_title="Intelligent Document Query Agent", layout="wide")

# Session state to store document path and initialization status
if 'agent_initialized' not in st.session_state:
    st.session_state.agent_initialized = False
if 'pdf_path' not in st.session_state:
    st.session_state.pdf_path = None

st.title("📚 Intelligent Document Query Agent")
st.markdown("Upload a PDF document and ask questions about its content!")

# --- Document Upload and Initialization ---
st.header("1. Upload Document")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded file temporarily
    temp_pdf_path = os.path.join("temp", uploaded_file.name)
    os.makedirs("temp", exist_ok=True) # Ensure temp directory exists
    with open(temp_pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.session_state.pdf_path = temp_pdf_path
    st.success(f"Document '{uploaded_file.name}' uploaded successfully!")

    if st.button("Initialize Agent with Document"):
        with st.spinner("Initializing agent... This may take a moment for larger documents and LLM setup."):
            try:
                initialize_agent(st.session_state.pdf_path)
                st.session_state.agent_initialized = True
                st.success("Agent initialized and ready to answer questions!")
                if llm is None:
                    st.warning("Warning: LLM could not be connected. Please ensure Ollama is running and the model (llama3) is downloaded. You can still try, but answers might fail.")
            except Exception as e:
                st.error(f"Error during agent initialization: {e}")
                st.session_state.agent_initialized = False
else:
    st.session_state.agent_initialized = False
    st.session_state.pdf_path = None


# --- Querying the Agent ---
st.header("2. Ask a Question")

if st.session_state.agent_initialized:
    user_question = st.text_input("Your question:", placeholder="e.g., What is the main topic of this document?")
    
    if st.button("Get Answer"):
        if user_question:
            with st.spinner("Agent thinking..."):
                answer = query_agent(user_question)
                st.write("---")
                st.subheader("Agent's Answer:")
                st.info(answer)
                st.write("---")
        else:
            st.warning("Please enter a question.")
else:
    st.info("Please upload a PDF and initialize the agent first.")

st.markdown("---")
st.caption("Built with Python, PyPDF2, Sentence Transformers, FAISS, Ollama, and Streamlit.")
st.caption("Ensure Ollama is running and the 'llama3' model is downloaded for full functionality.")