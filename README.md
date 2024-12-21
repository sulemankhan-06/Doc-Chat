# RAG-Powered Documentation Assistant

A sophisticated Retrieval-Augmented Generation (RAG) system that provides intelligent responses to queries about various documentation frameworks including LangChain, LlamaIndex, and Haystack. Built with Streamlit, this application leverages the power of Groq's Gemma model and Mistral's embedding capabilities.

## 🌟 Features

- **Real-time Documentation Processing**: Efficiently processes and indexes documentation from multiple sources
- **Advanced RAG Pipeline**: Implements a state-of-the-art retrieval-augmented generation system
- **Interactive Web Interface**: Clean and responsive UI built with Streamlit
- **Modular Architecture**: Well-structured codebase with separation of concerns
- **Configurable Components**: Easily adjustable parameters for document processing and model behavior

## 🛠️ Technology Stack

- **Framework**: Streamlit
- **LLM Provider**: Groq (Gemma 2-9B)
- **Embeddings**: Mistral AI
- **Vector Store**: FAISS
- **Document Processing**: LangChain
- **Python**: 3.8+

## 📋 Prerequisites

- Python 3.8 or higher
- API keys for:
  - Groq
  - Mistral AI
  - LangChain (for tracing)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/rag-documentation-assistant.git
cd rag-documentation-assistant
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

## ⚙️ Configuration

Create a `.env` file in the root directory with the following variables:

```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langchain_api_key
GROQ_API_KEY=your_groq_api_key
MISTRALAI_API_KEY=your_mistral_api_key
```

Additional configurations can be modified in `config.py`:
- Document chunk size
- Chunk overlap
- Model selections
- Documentation sources

## 🖥️ Usage

1. Start the application:
```bash
streamlit run src/app.py
```

2. Access the web interface at `http://localhost:8501`

3. Enter your query about any of the supported documentation frameworks

## 📁 Project Structure

```
project_root/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── config.py       # Configuration settings
│   ├── utils.py        # Utility functions
│   ├── chain_builder.py # RAG chain construction
│   └── app.py          # Streamlit application
└── tests/
    └── __init__.py
```

## 🔧 Components

### Document Processor
- Handles document loading from URLs
- Implements text splitting with configurable chunk sizes
- Creates and manages FAISS vector store

### Chain Builder
- Constructs the RAG pipeline
- Manages prompt templates
- Integrates LLM and retrieval components

### Configuration Management
- Centralizes all configurable parameters
- Manages environment variables
- Provides type-safe config access

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your PR adheres to:
- Consistent code style
- Appropriate test coverage
- Updated documentation
- Clear commit messages

## 📝 API Documentation

### DocumentProcessor

```python
DocumentProcessor(urls: List[str], chunk_size: int, chunk_overlap: int)
```

**Parameters:**
- `urls`: List of documentation URLs to process
- `chunk_size`: Size of text chunks for processing
- `chunk_overlap`: Overlap between consecutive chunks

### build_retrieval_chain

```python
build_retrieval_chain(vector_store, llm_model: str)
```

**Parameters:**
- `vector_store`: FAISS vector store instance
- `llm_model`: Name of the LLM model to use

## ⚠️ Known Limitations

- Currently only supports web-based documentation sources
- Rate limits based on API provider constraints
- Memory usage scales with document size

## 🔒 Security

- API keys are managed through environment variables
- Input validation is implemented for all user inputs
- Rate limiting is applied to API calls

## 📈 Future Improvements

- [ ] Add support for PDF documentation
- [ ] Implement caching for frequent queries
- [ ] Add multi-language support
- [ ] Enhance error handling and recovery
- [ ] Implement batch processing for large documents

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- sulemankhan-06 - *Initial work* - [YourGitHub](https://github.com/sulemankhan-06/)

---

**Note**: For production deployment, ensure all API keys are properly secured and consider implementing additional security measures.