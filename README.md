# 🤖 Customer Service Chatbot

A Streamlit-based AI chatbot that uses LangChain, Google Palm, and FAISS to answer customer queries from a CSV knowledge base.

## 🚀 Features

- Ask natural language questions  
- Build a knowledge base from a CSV file  
- Get relevant answers using embeddings and vector search  
- Uses Google Palm as the language model  

## 🧰 Tech Stack

- Streamlit  
- LangChain  
- Google Palm API  
- FAISS  
- HuggingFace Embeddings  
- Python  

## 📂 Project Structure

```
.
├── main.py                  # Streamlit UI  
├── langchain_helper.py     # Vector DB & QA logic  
├── requirements.txt         # Python dependencies  
├── dataset.csv              # CSV knowledge base  
└── .env                     # API keys (not included in repo)  
```

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/customer-service-chatbot.git
cd customer-service-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project directory with:

```
GOOGLE_API_KEY=your_google_palm_api_key
```

> Replace `your_google_palm_api_key` with your actual Google Palm API key.

### 5. Add Your Dataset

Update the file path in `langchain_helper.py`:

```python
loader = CSVLoader(file_path=r"PATH_TO_YOUR_CSV", source_column="prompt")
```

Ensure your CSV has `prompt` and `response` columns.

### 6. Run the App

```bash
streamlit run main.py
```

## 🧠 How It Works

- Loads and chunks CSV content  
- Embeds chunks using HuggingFace embeddings  
- Indexes with FAISS  
- Uses LangChain’s RetrievalQA to query Google Palm with the relevant context  

## 📌 Example

**Question:** _How do I reset my password?_  
**Answer:** _Please refer to the password reset section in your account settings or contact support._

## 📄 License

MIT License

