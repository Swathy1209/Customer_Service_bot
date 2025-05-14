🤖 Customer Service Chatbot



A Streamlit-based AI chatbot that leverages LangChain, Google Palm, and FAISS for intelligent question-answering from a CSV-based knowledge base. Ideal for enhancing customer support by enabling automated yet accurate responses.

🚀 Features
💬 Ask natural language questions.

📚 Create a vectorized knowledge base from your CSV data.

🔍 Retrieves highly relevant answers based on context.

🤖 Powered by Google Palm and HuggingFace embeddings.

🧰 Tech Stack
Streamlit – UI for interacting with the bot

LangChain – Framework for chaining LLMs

Google Palm – LLM provider

FAISS – Vector similarity search

HuggingFace Embeddings – Document embeddings

📂 Folder Structure
bash
Copy
Edit
├── main.py                  # Streamlit app entry point
├── langchain_helper.py     # LangChain pipeline and vector DB logic
├── .env                    # API keys and environment variables
└── dataset.csv             # Your source CSV file (update path in code)
⚙️ Setup Instructions
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/yourusername/customer-service-chatbot.git
cd customer-service-chatbot
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Example requirements.txt:

txt
Copy
Edit
streamlit
langchain
faiss-cpu
python-dotenv
huggingface_hub
4. Set Up .env File
Create a .env file in the root directory:

env
Copy
Edit
GOOGLE_API_KEY=your_google_palm_api_key
Update the API key used in langchain_helper.py if hardcoded.

5. Add Your Dataset
Place your CSV dataset in the appropriate directory and update this line in langchain_helper.py:

python
Copy
Edit
loader = CSVLoader(file_path=r"PATH_TO_YOUR_CSV", source_column="prompt")
Make sure the file contains prompt and response columns.

6. Run the App
bash
Copy
Edit
streamlit run main.py
📝 Usage
Click "create knowledgebase" to generate the FAISS vector store.

Enter your query in the text box.

View the contextual AI-generated answer.

🧠 How It Works
Loads and chunks CSV content.

Embeds chunks using HuggingFaceInstructEmbeddings.

Indexes with FAISS.

Uses LangChain's RetrievalQA to retrieve context and query Google Palm for answers.

📌 Example Question
Question: How do I reset my password?

Answer: Please refer to the password reset section in your account settings or contact support.

📄 License
MIT License
