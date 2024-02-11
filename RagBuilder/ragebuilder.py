from pprint import pprint 
from langchain import PromptTemplate 
from langchain.chains.question_answering import load_qa_chain 
from langchain.document_loaders import PyPDFLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain.vectorstores import Chroma 
from langchain.chains import RetrievalQA 
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from .utils import to_markdown

class LangchainGemeni:

    def __init__(self, GOOGLE_API_KEY:str,temperature:float) -> None:
        self.GOOGLE_API_KEY = GOOGLE_API_KEY
        self.client =ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=GOOGLE_API_KEY, temperature=temperature,convert_system_message_to_human=True) 

    def GenerateContent(self, prompt:str)-> str: 
        response = self.client.invoke(prompt)
        return response
    



    def AIEmbeddingsPdfPages2Vector(self,pdf:str)->object:
        pdf_loader = PyPDFLoader(pdf)
        pages = pdf_loader.load_and_split()
        self.pdf_pages = pages
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)    
        context = "\n\n".join(str(p.page_content) for p in self.pdf_pages)
        texts = text_splitter.split_text(context) 
        embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001",google_api_key=self.GOOGLE_API_KEY)
        vector_index = Chroma.from_texts(texts, embeddings).as_retriever()
        self.vector_index = vector_index
        return  vector_index  


    def BuildQA(self,return_source_documents=True)->object:
        qa_chain = RetrievalQA.from_chain_type( self.client, retriever=self.vector_index, return_source_documents=return_source_documents)
        return qa_chain 