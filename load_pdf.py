from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import streamlit as st
import tempfile


def pdfs():

    uploaded_pdfs = st.file_uploader(
        "Upload PDFs",
        type="pdf",
        accept_multiple_files=True
    )

    if not uploaded_pdfs:
        return None

    all_documents = []

    for pdf in uploaded_pdfs:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(pdf.read())
            temp_path = temp_file.name

        loader = PyPDFLoader(temp_path)
        documents = loader.load()

        all_documents.extend(documents)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    texts = text_splitter.split_documents(all_documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(texts, embeddings)

    retriever = vectorstore.as_retriever(search_kwargs={"k": 25})
    st.write("### Uploaded Files")

    for pdf in uploaded_pdfs:
        st.write("📄", pdf.name)

    return retriever