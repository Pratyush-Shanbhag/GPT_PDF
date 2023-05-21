from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

import streamlit as st


txt_path = "ocr_text_filtered.txt"
loader =  TextLoader(txt_path, encoding='utf8')
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