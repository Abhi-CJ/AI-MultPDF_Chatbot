from dotenv import load_dotenv
import streamlit as st
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
load_dotenv()
 


st.title("AI Text Summarizer")

text = st.text_area("Enter your text")

if st.button("Summarize"):
    if text:
        llm = HuggingFaceEndpoint(repo_id = 'Qwen/Qwen3-Coder-Next',
                         temperature = 0,
                         max_new_tokens=200,
                         )
        
        model = ChatHuggingFace(llm = llm)
        
        prompt = f'''
        You are a professional summarizer.
        Summarize the following text:\n{text} by including paragraph or bullet points. 
        Summary should be about 10 % of original text.''' 
        with st.spinner("Generating summary..."):
            response = model.invoke(prompt)
        
            st.subheader('Summary')
            st.write(response.content)
        
    else:
        st.warning('Write Text to summarize')
    










