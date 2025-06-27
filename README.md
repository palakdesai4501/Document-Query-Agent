# 📚 Intelligent Document Query Agent

An AI-powered document query system that allows users to upload PDF documents and ask questions about their content using Retrieval-Augmented Generation (RAG). Built with Python, Streamlit, and Ollama.

## 🌟 Features

- **PDF Document Processing**: Extract text from PDF files using PyPDF2
- **Semantic Search**: Uses sentence transformers to create embeddings for semantic similarity
- **Vector Database**: FAISS-powered vector storage for efficient similarity search
- **Local LLM Integration**: Powered by Ollama with llama3 model for privacy-focused AI responses
- **Interactive Web Interface**: Clean and intuitive Streamlit-based UI
- **RAG Architecture**: Combines document retrieval with generative AI for accurate, context-aware answers

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **PDF Processing**: PyPDF2
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **Vector Database**: FAISS
- **LLM**: Ollama (llama3)
- **Language**: Python 3.8+

## 📋 Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed and running
- Git (for cloning the repository)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd document_query_agent
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install and setup Ollama**
   - Download and install Ollama from [https://ollama.ai/](https://ollama.ai/)
   - Pull the llama3 model:
     ```bash
     ollama pull llama3
     ```
   - Start Ollama service:
     ```bash
     ollama serve
     ```

## 🎯 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - Navigate to `http://localhost:8501`

3. **Upload and query your document**
   - Click "Choose a PDF file" to upload your document
   - Click "Initialize Agent with Document" to process the PDF
   - Wait for the success message "Agent initialized and ready to answer questions!"
   - Type your question in the text input field
   - Click "Get Answer" to receive AI-generated responses

## 📁 Project Structure

```
document_query_agent/
├── app.py                      # Streamlit web application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore patterns
├── documents/                  # Sample documents
│   └── sample.pdf
├── src/                        # Source code modules
│   ├── agent.py               # Main agent logic and RAG implementation
│   ├── document_processor.py  # PDF text extraction
│   ├── embeddings_generator.py # Text embedding creation
│   ├── vector_store.py        # FAISS vector database operations
│   └── my_document_index.faiss # Generated FAISS index (ignored in git)
├── temp/                      # Temporary uploaded files (ignored in git)
└── venv/                      # Virtual environment (ignored in git)
```

## 🔧 Configuration

### Model Configuration
- Default LLM: `llama3`
- Embedding Model: `all-MiniLM-L6-v2`
- Vector Search: Top 2 most similar chunks
- LLM Temperature: 0.1 (for factual responses)

### Customization
You can modify the following in `src/agent.py`:
- Change the LLM model by updating the `llm_model_name` parameter
- Adjust the number of retrieved chunks by modifying the `k` parameter in `search_faiss_index`
- Modify the prompt template for different response styles

## 🧠 How It Works

1. **Document Processing**: PDFs are parsed and text is extracted page by page
2. **Embedding Generation**: Text chunks are converted to numerical vectors using sentence transformers
3. **Vector Storage**: Embeddings are stored in a FAISS index for fast similarity search
4. **Query Processing**: User questions are embedded and matched against document chunks
5. **Context Retrieval**: Most relevant document sections are retrieved
6. **Answer Generation**: Ollama LLM generates responses based on retrieved context

## 🚨 Troubleshooting

### Common Issues

**Port 11434 already in use**
```bash
# Find and kill the process
lsof -i :11434
kill -9 <PID>
```

**Ollama model not found**
```bash
# Pull the required model
ollama pull llama3
```

**Agent not initialized error**
- Ensure you clicked "Initialize Agent with Document" before asking questions
- Verify Ollama is running and accessible
- Check that the PDF was uploaded successfully

**Import errors**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify you're in the correct virtual environment

## 📝 Dependencies

```
streamlit
PyPDF2
sentence-transformers
faiss-cpu
langchain_community
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai/) for local LLM capabilities
- [Streamlit](https://streamlit.io/) for the web interface framework
- [Sentence Transformers](https://www.sbert.net/) for embedding generation
- [FAISS](https://faiss.ai/) for efficient vector similarity search
- [LangChain](https://langchain.com/) for LLM integration patterns

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub or contact the maintainer.

---

Built with ❤️ using Python, AI, and open-source technologies.
