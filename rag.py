from langchain.chains import (
    create_history_aware_retriever,
    create_retrieval_chain,
)
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

import os
from dotenv import load_dotenv
from langchain import hub
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings
from langchain_groq import ChatGroq



class RAGModule:
    def __init__(self, pdf_path="docs/cv.pdf"):
        load_dotenv()
        
        # Initialize components
        self.loader = PyPDFLoader(pdf_path)
        self.document = self.loader.load()
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.splits = self.text_splitter.split_documents(self.document)
        self.vectorstore = Chroma.from_documents(documents=self.splits, embedding=FastEmbedEmbeddings())
        self.retriever = self.vectorstore.as_retriever()
        
        self.llm = ChatGroq(
            model="llama-3.2-1b-preview",
            temperature=0.6,
            max_tokens=300,
            api_key=os.getenv("GROQ_API_KEY"),
        )
        
        # Set up the chain
        self.setup_chain()
        
    def setup_chain(self):
        # Contextualize question
        contextualize_q_system_prompt = (
            "Given a chat history and the latest user question "
            "which might reference context in the chat history, "
            "formulate a standalone question which can be understood "
            "without the chat history. Do NOT answer the question, just "
            "reformulate it if needed and otherwise return it as is."
        )
        
        contextualize_q_prompt = ChatPromptTemplate.from_messages([
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ])
        
        history_aware_retriever = create_history_aware_retriever(
            self.llm, self.retriever, contextualize_q_prompt
        )
        
        qa_system_prompt = (
            "You are an assistant for question-answering tasks. Your responses "
            "should be related to the data scientist Moudathirou Ben Saindou, "
            "and based on his provided CV, which is attached. Use the following "
            "pieces of retrieved context to answer the question. If you don't know "
            "the answer, just say that you don't know. Use three sentences maximum "
            "and keep the answer concise."
            "{context}"
        )


        
        
        qa_prompt = ChatPromptTemplate.from_messages([
            ("system", qa_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ])
        
        question_answer_chain = create_stuff_documents_chain(self.llm, qa_prompt)
        
        self.rag_chain = create_retrieval_chain(
            history_aware_retriever, question_answer_chain
        )
    
    def get_response(self, user_message, chat_history):
        return self.rag_chain.invoke({
            "input": user_message,
            "chat_history": chat_history
        })