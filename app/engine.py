import os
from langchain_groq import ChatGroq
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

class HAIEngine:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.db = Chroma(persist_directory="./db", embedding_function=self.embeddings)

    def get_response(self, query):
        retriever = self.db.as_retriever(search_kwargs={"k": 3})
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm, chain_type="stuff",
            retriever=retriever, return_source_documents=True
        )
        result = qa_chain({"query": query})
        return result["result"], result["source_documents"]
      
