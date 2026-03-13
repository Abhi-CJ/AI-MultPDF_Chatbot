import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()


prompt = PromptTemplate(
    input_variables=["topic"],
    template='''You are a professional blogger.
    Write a short blog about {topic}.
    Structure Blog with:
            -title
            -introduction
            - 5 main points(Short Explanation)
            - conclusion
            '''
)


st.title("Blog Post or Article Generator")

topic = st.text_input("Enter your topic")

if st.button("Generate Blog"):
    if topic:
        llm = HuggingFaceEndpoint(repo_id='Qwen/Qwen3-Coder-Next',
                         temperature = 0,
                          
                         max_new_tokens=500,
                         )
        
        model = ChatHuggingFace(llm = llm)
        
        with st.spinner("Generating Blog..."):
            response = model.invoke(prompt.format(topic = topic))
        
            st.subheader('Blog')
            st.write(response.content)
        
    else:
        st.warning('Please Enter a Topic')
    







