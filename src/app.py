import streamlit as st
from src.config import Config
from src.utils import DocumentProcessor
from src.chain import build_retrieval_chain
from langchain_mistralai import MistralAIEmbeddings

def initialize_session_state():
    if 'vector' not in st.session_state:
        embeddings = MistralAIEmbeddings(
            model=Config.EMBEDDING_MODEL,
            api_key=Config.MISTRALAI_API_KEY
        )
        
        processor = DocumentProcessor(
            urls=Config.DOCUMENTATION_URLS,
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP
        )
        
        st.session_state.vector = processor.load_and_process_documents(embeddings)

def main():
    st.title("Doc Chat Assistant")
    
    initialize_session_state()
    retrieval_chain = build_retrieval_chain(
        st.session_state.vector,
        Config.LLM_MODEL
    )
    
    prompt = st.text_input('Ask a question about the documentation')
    
    if prompt:
        response = retrieval_chain.invoke({'input': prompt})
        st.write(response['answer'])
        
        with st.expander("Document Similarity Search"):
            for i, doc in enumerate(response["context"]):
                st.write(doc.page_content)
                st.write("---")

if __name__ == "__main__":
    main()