from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    LANGCHAIN_TRACING_V2 = 'true'
    LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MISTRALAI_API_KEY = os.getenv("MISTRALAI_API_KEY")
    
    # Model configurations
    EMBEDDING_MODEL = "mistral-embed"
    LLM_MODEL = "gemma2-9b-it"
    
    # Document processing
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    
    # Data sources
    DOCUMENTATION_URLS = [
        'https://docs.smith.langchain.com/',
        'https://python.langchain.com/docs/introduction/',
        'https://docs.llamaindex.ai/en/stable/',
        'https://docs.haystack.deepset.ai/v1.26/docs/intro'
    ]