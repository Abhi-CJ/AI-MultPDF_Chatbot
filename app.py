from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import streamlit as st
from dotenv import load_dotenv
from load_pdf import pdfs

load_dotenv()

st.title('AI PDF CHATBOT')
retriever = pdfs()




llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    max_new_tokens=400,
    temperature=0.3
)
model = ChatHuggingFace(llm =llm)


if retriever is None:
    st.info("Please upload PDF files first.")
else:
    question = st.text_input("Ask a question about the PDF")
    
   
    if question and retriever:
        with st.spinner('Thinking...'):
                docs = retriever.invoke(question)
                context = "\n".join([doc.page_content for doc in docs])
    
                prompt = PromptTemplate(input_variables = ['context', 'question'],
                            template = '''
                            Answer the question using the provided context.
                            Context:
                            {context}
                            Question:
                            {question}
                            Answer: 
                            '''
                            )
                final_prompt = prompt.format(question = question,context = context)
        
    
                response = model.invoke(final_prompt)
                with st.chat_message("user"):
                    st.write(question)
                with st.chat_message('assistant'):
                    st.write(response.content)
                