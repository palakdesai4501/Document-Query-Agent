# 📚 Document Query Agent

AI-powered PDF document analysis using RAG (Retrieval-Augmented Generation). Upload PDFs and ask questions about their content.

## Features

- Upload PDF documents via web interface
- Ask natural language questions about document content
- Local AI processing (privacy-focused)
- Semantic search with vector embeddings

## Quick Start

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.ai/) installed

### Installation

1. **Clone and setup**
   ```bash
   git clone <repo-url>
   cd document_query_agent
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Setup Ollama**
   ```bash
   ollama pull llama3
   ollama serve  # Keep running in background
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

4. **Use the app**
   - Open http://localhost:8501
   - Upload a PDF
   - Click "Initialize Agent with Document"
   - Ask questions about your document

## Tech Stack

- **Frontend**: Streamlit
- **PDF Processing**: PyPDF2
- **Embeddings**: Sentence Transformers
- **Vector Store**: FAISS
- **LLM**: Ollama (llama3)

## Project Structure

```
document_query_agent/
├── app.py                     # Streamlit web app
├── requirements.txt           # Dependencies
├── src/
│   ├── agent.py              # Main RAG logic
│   ├── document_processor.py # PDF text extraction
│   ├── embeddings_generator.py # Text embeddings
│   └── vector_store.py       # FAISS operations
└── documents/                # Sample PDFs
```

## Troubleshooting

**"Port already in use" error**
```bash
lsof -i :11434
kill -9 <PID>
```

**"Model not found" error**
```bash
ollama pull llama3
```

**"Agent not initialized" error**
- Upload PDF first
- Click "Initialize Agent with Document"
- Ensure Ollama is running

## How It Works

1. Extract text from PDF pages
2. Create embeddings for text chunks
3. Store embeddings in FAISS vector database
4. For queries: find similar chunks → send to LLM → get answer

---

Built with Python • Streamlit • Ollama • FAISS
