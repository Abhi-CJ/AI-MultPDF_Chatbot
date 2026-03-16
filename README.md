# AI PDF Chatbot (RAG) using LangChain, FAISS & HuggingFace

## Overview

The **AI PDF Chatbot** is a Generative AI application that allows users to upload a PDF document and ask questions about its content.

The system retrieves the most relevant information from the document and generates answers using a **Large Language Model (LLM)**.

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline using:

* LangChain
* FAISS Vector Database
* HuggingFace Embeddings
* HuggingFace LLM Endpoint
* Streamlit UI

This project demonstrates how modern **AI-powered document assistants** work.

---

## Features

* Upload and process PDF documents
* Extract text automatically
* Intelligent document chunking
* Generate embeddings using HuggingFace models
* Store embeddings in FAISS vector database
* Retrieve relevant document chunks
* Generate context-aware answers using LLM
* Interactive Streamlit web interface

---

## How the System Works

1. User uploads a PDF document
2. The document is loaded using **PyPDFLoader**
3. Text is split into smaller chunks
4. Each chunk is converted into **vector embeddings**
5. Embeddings are stored in a **FAISS vector database**
6. When a question is asked:

   * The retriever finds the most relevant chunks
   * These chunks are sent to the LLM as context
   * The LLM generates an answer based on the document

---

## Architecture (RAG Pipeline)

```
User Upload PDF
        │
        ▼
Document Loader (PyPDFLoader)
        │
        ▼
Text Splitter
        │
        ▼
Embeddings (HuggingFace)
        │
        ▼
FAISS Vector Database
        │
        ▼
Retriever
        │
        ▼
Prompt + Context
        │
        ▼
LLM (Llama 3.1 via HuggingFace)
        │
        ▼
Generated Answer
```

This architecture is called **Retrieval-Augmented Generation (RAG)**.

---

## Tech Stack

| Technology             | Purpose                         |
| ---------------------- | ------------------------------- |
| Python                 | Programming Language            |
| Streamlit              | Web Interface                   |
| LangChain              | LLM Application Framework       |
| FAISS                  | Vector Database                 |
| HuggingFace Embeddings | Text Embeddings                 |
| HuggingFace Endpoint   | Large Language Model            |
| PyPDFLoader            | PDF Document Loader             |
| Dotenv                 | Environment Variable Management |

---

## Project Structure

```
GEN_AI/
│
├── app.py              # Main Streamlit chatbot application
├── load_pdf.py         # PDF loading and vector database creation
├── requirements.txt    # Project dependencies
├── .env                # HuggingFace API token
├── README.md           # Project documentation
│
├── venv/
└── __pycache__/
```

### File Description

| File                 | Description                                                                   |
| -------------------- | ----------------------------------------------------------------------------- |
| **app.py**           | Streamlit application that handles user interaction and chatbot responses     |
| **load_pdf.py**      | Loads PDFs, splits text, creates embeddings, and builds FAISS vector database |
| **requirements.txt** | Contains all project dependencies                                             |
| **.env**             | Stores HuggingFace API token securely                                         |

---

## Installation

### Clone the Repository

```
git clone https://github.com/yourusername/ai-MultiPDF-chatbot.git
cd ai-pdf-chatbot
```

---

### Create Virtual Environment

```
python -m venv venv
```

Activate it:

**Windows**

```
venv\Scripts\activate
```

---

### Install Dependencies

```
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

```
streamlit run app.py
```

The application will automatically open in your browser.

---

## Example Usage

1. Upload a PDF document
2. Ask questions such as:

* *"Summarize this document"*
* *"What topics are covered?"*
* *"Explain the main concepts"*

3. The chatbot will generate answers based on the uploaded PDF content.

---

## Learning Outcomes

Through this project you will learn:

* Retrieval-Augmented Generation (**RAG**)
* Document processing using **LangChain**
* Semantic search with **vector databases**
* Embeddings and similarity search
* Integrating **LLMs** into applications
* Building AI apps using **Streamlit**

---

## Future Improvements

* **Conversation memory**
* **Persistent vector database**
* **Source citations with page numbers**
* **Streaming LLM responses**

---

## Author

**Abhishek Jain**

Aspiring **AI / Python Developer** focused on building practical **Generative AI applications** using LangChain and modern LLM frameworks.

---

## Support the Project

If you found this project helpful, please consider giving it a **Star ⭐ on GitHub**.

It helps the project reach more developers and motivates further improvements.
