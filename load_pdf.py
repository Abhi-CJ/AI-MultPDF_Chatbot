from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import streamlit as st
import tempfile
def pdf():
    
    pdf = st.file_uploader('Upload PDF', type = 'pdf')
    if pdf is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(pdf.read())
            temp_path = tmp_file.name
        

        loader = PyPDFLoader(temp_path)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 500,
            chunk_overlap = 50

    )
        texts = text_splitter.split_documents(documents)
   
        embeddings = HuggingFaceEmbeddings()
        vectorstore = FAISS.from_documents(texts, embeddings)
        retriever = vectorstore.as_retriever(search_kwargs={"k":3})
        return retriever
