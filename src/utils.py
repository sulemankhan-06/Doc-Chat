from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from typing import List, Dict

class DocumentProcessor:
    def __init__(self, urls: List[str], chunk_size: int, chunk_overlap: int):
        self.urls = urls
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
    
    def load_and_process_documents(self, embeddings):
        loader = WebBaseLoader(web_paths=self.urls)
        documents = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )
        split_documents = text_splitter.split_documents(documents)
        
        vector_store = FAISS.from_documents(split_documents, embeddings)
        return vector_store