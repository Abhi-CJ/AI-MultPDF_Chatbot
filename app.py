from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import streamlit as st
from dotenv import load_dotenv
from load_pdf import pdf

load_dotenv()

st.title('AI PDF CHATBOT')
retriever = pdf()

question = st.text_input("Ask a question about the PDF")
if question:
        docs = retriever.invoke(question)
        context = "\n".join([doc.page_content for doc in docs])
    
        llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    max_new_tokens=400,
    temperature=0.3
)
        model = ChatHuggingFace(llm =llm)
        prompt = PromptTemplate(input_variables = ['context', 'question'],
                            template = '''Answer the question using the provided context
                            Context:{context}
                            Questoin: {question}
                            Ansswer: 
                            '''
                            )
        final_prompt = prompt.format(question = question,context = context)
        response = model.invoke(final_prompt)
        st.write(response.content)