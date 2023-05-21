from langchain.document_loaders import UnstructuredPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

import streamlit as st


pdf_path = "bill.pdf"
loader =  UnstructuredPDFLoader(pdf_path)
pages = loader.load_and_split()

#print(pages[2].page_content)

embeddings = OpenAIEmbeddings()
vectorstore =  Chroma.from_documents(pages, embedding=embeddings, persist_directory='.').as_retriever()

llm = ChatOpenAI(temperature=0.9, model_name='gpt-3.5-turbo')
chain = ConversationalRetrievalChain.from_llm(llm, vectorstore)


st.title('PDF Reader')
prompt = st.text_input('Enter Prompt:')

if prompt:
    result = chain({'question': prompt, 'chat_history': ''})
    st.write(result['answer'])