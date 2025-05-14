from langchain_community.vectorstores import FAISS
from langchain_community.llms import GooglePalm
from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize LLM
llm = GooglePalm(google_api_key=os.getenv("AIzaSyCvjl5Th6wbLcUGubVmZDSQMWrLiewJM7I"), temperature=0.1)

# Initialize Embeddings
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")

# FAISS Index File Path
vectordb_file_path = "faiss_index"

def create_vector_db():
    loader = CSVLoader(file_path=r"C:\Users\swathiga\Downloads\Dataset\dataset.csv", source_column="prompt")


    data = loader.load()
    
    # Split text into chunks before embedding
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents = text_splitter.split_documents(data)
    
    # Create FAISS vector store
    vectordb = FAISS.from_documents(documents, instructor_embeddings)
    vectordb.save_local(vectordb_file_path)

def get_qa_chain():
    # Load FAISS database with embeddings
    vectordb = FAISS.load_local(vectordb_file_path, embeddings=instructor_embeddings)
    retriever = vectordb.as_retriever(score_threshold=0.7)
    
    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer, try to provide as much text as possible from the "response" section in the source document without making major changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}
    """

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # Create RetrievalQA Chain
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )
    
    return chain

if __name__ == "__main__":
    create_vector_db()  # Create vector database
    chain = get_qa_chain()  # Get the QA Chain
    print(chain("Who are you?"))  # Test the system
