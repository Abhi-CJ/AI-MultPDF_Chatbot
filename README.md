# 🤖 AI Blog Generator using LangChain and HuggingFace

An AI-powered web application that automatically generates structured blog posts from a user-provided topic.  
The application uses **LangChain Prompt Templates**, **HuggingFace Large Language Models**, and **Streamlit** to create high-quality blog content in seconds.

---

## 📌 Project Overview

The **AI Blog Generator** allows users to input a topic and instantly generate a complete blog post including:

- Title
- Introduction
- 5 Main Points (with short explanations)
- Conclusion

This project demonstrates how **Generative AI and Large Language Models (LLMs)** can be used to automate content creation workflows.

---

## 🚀 Features

- Generate blog articles from any topic
- Structured blog format
- Uses **LangChain Prompt Templates**
- Integrates **HuggingFace LLM API**
- Interactive **Streamlit web interface**
- Fast and simple content generation

---

## 🛠 Tech Stack

- **Python**
- **LangChain**
- **HuggingFace Inference API**
- **Streamlit**
- **python-dotenv**

---

## 📂 Project Structure
AI-Blog-Generator
│
├── app.py
├── requirements.txt
├── .env
└── README.md


---

## ⚙️ Installation

### 1️⃣ Clone the Repository
git clone https://github.com/Abhi-CJ/ai-blog-generator-langchain.git


### 2️⃣ Navigate to the Project Folder
cd ai-blog-generator-langchain


### 3️⃣ Create a Virtual Environment
python -m venv venv


### 4️⃣ Activate Virtual Environment

Windows
venv\Scripts\activate


Mac/Linux
source venv/bin/activate

---

### 5️⃣ Install Dependencies
pip install -r requirements.txt


---

## 🔑 Environment Variables

Create a `.env` file in the project root folder and add:

HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token


You can get your API key from:

https://huggingface.co/settings/tokens

---

## ▶️ Running the Application

Start the Streamlit app with:




After running the command, the application will open in your browser.

---

## 🧠 How It Works

1. User enters a topic in the input field.
2. LangChain **PromptTemplate** structures the request.
3. The HuggingFace model generates blog content.
4. Streamlit displays the generated blog post in the UI.

---

## 📝 Example

### Input



### Output

- Blog Title  
- Introduction  
- 5 Key Points with Explanation  
- Conclusion  

---

## 📈 Future Improvements

Some potential improvements for this project:

- Add blog length customization
- Add SEO keyword generation
- Export blog to **PDF or Markdown**
- Add multiple writing styles
- Integrate advanced LLM models

---

## 👨‍💻 Author

**Abhishek Jain**

Python Developer | Generative AI Enthusiast

---

## ⭐ Support

If you found this project useful, please consider giving the repository a **star ⭐ on GitHub**.




