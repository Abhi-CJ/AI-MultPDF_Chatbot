# AI PDF Chatbot (RAG) using LangChain, FAISS & HuggingFace

## Project Overview

The **AI PDF Chatbot** is a Generative AI application that allows users to upload a PDF document and ask questions about its content. The system retrieves relevant information from the document and generates accurate answers using a Large Language Model (LLM).

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline using LangChain, FAISS, and HuggingFace models with a Streamlit interface.

---

## Features

* Upload any PDF document
* Automatically extract and process document content
* Split large text into manageable chunks
* Generate embeddings using HuggingFace models
* Store embeddings in a FAISS vector database
* Retrieve relevant document sections for user queries
* Generate context-aware answers using an LLM
* Simple and interactive Streamlit interface

---

## How It Works

1. User uploads a PDF document
2. The PDF is loaded using **PyPDFLoader**
3. Text is split into smaller chunks
4. Each chunk is converted into **vector embeddings**
5. Embeddings are stored in **FAISS vector database**
6. When a question is asked:

   * The retriever finds the most relevant chunks
   * The LLM uses those chunks as context
   * The chatbot generates an answer

---

## Architecture

PDF Upload
↓
Document Loader
↓
Text Splitter
↓
Embeddings (HuggingFace)
↓
FAISS Vector Store
↓
Retriever
↓
LLM Response

This architecture is known as **Retrieval-Augmented Generation (RAG)**.

---

## 🛠 Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **FAISS Vector Database**
* **HuggingFace Embeddings**
* **HuggingFace LLM Endpoint**
* **PyPDF**
* **Dotenv**

---

## Project Structure

```
GEN_AI/
│
├── app.py              # Main Streamlit application
├── load_pdf.py         # PDF loading and vector database creation
├── requirements.txt    # Project dependencies
├── .env                # HuggingFace API token
├── venv                # Virtual environment
└── __pycache__         # Python cache files
```

---

## ⚙ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/ai-pdf-chatbot.git
cd ai-pdf-chatbot
```

---

### Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Add HuggingFace API Token

Create a `.env` file in the project root:

```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

You can generate a token from:
https://huggingface.co/settings/tokens

---

## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Example Usage

1. Upload a PDF file
2. Ask questions like:

   * "What topics are covered in this document?"
   * "Summarize the key points"
   * "Explain the main concepts"

The chatbot will answer based on the PDF content.

---

## Learning Outcomes

Through this project you will learn:

* Retrieval-Augmented Generation (RAG)
* Document processing with LangChain
* Vector databases (FAISS)
* Embedding models
* LLM integration
* Building AI apps using Streamlit

---

## Future Improvements

* Chat memory support
* Multiple PDF support
* Persistent vector database
* Better UI with chat interface
* Streaming responses

---

## Author

**Abhishek Jain**

Aspiring **AI / Python Developer** focused on building practical Generative AI applications using LangChain and modern LLM frameworks.

---

## If you found this project useful

Please consider giving the repository a **star ⭐ on GitHub**.
