'''from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI

from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)

import streamlit as st


pdf_path = "bill.pdf"
loader =  PyPDFLoader(pdf_path)
pages = loader.load_and_split()

#print(pages[2].page_content)

embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(temperature=0.9, model_name='gpt-3.5-turbo')

vectorstore =  Chroma.from_documents(pages, embedding=embeddings, persist_directory='.')

vectorstore_info = VectorStoreInfo(name='electricity_bill', description='electricity bill as a pdf', vectorstore=vectorstore)

toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

agent = create_vectorstore_agent(llm=llm, toolkit=toolkit, verbose=True)


st.title('PDF Reader')
prompt = st.text_input('Enter Prompt:')

if prompt:
    result = agent.run(prompt)
    st.write(result)'''


# Import OpenAI as main LLM service
from langchain.llms import OpenAI
# Bring in streamlit for UI/app interface
import streamlit as st

# Import PDF document loaders...there's other ones as well!
from langchain.document_loaders import PyPDFLoader
# Import chroma as the vector store 
from langchain.vectorstores import Chroma

# Import vector store stuff
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)

# Create instance of OpenAI LLM
llm = OpenAI(temperature=0.9, model_name='gpt-3.5-turbo', verbose=True)

# Create and load PDF Loader
loader = PyPDFLoader('../paper.pdf')
# Split pages from pdf 
pages = loader.load_and_split()

print(pages[0].page_content)

# Load documents into vector database aka ChromaDB
store = Chroma.from_documents(pages, collection_name='monthlyreport')

# Create vectorstore info object - metadata repo?
vectorstore_info = VectorStoreInfo(
    name="monthly_report",
    description="an electricity monthly report as a pdf",
    vectorstore=store
)
# Convert the document store into a langchain toolkit
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

# Add the toolkit to an end-to-end LC
agent_executor = create_vectorstore_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)
st.title('🦜🔗 GPT Electricity Bill Reader')
# Create a text input box for the user
prompt = st.text_input('Input your prompt here')

# If the user hits enter
if prompt:
    # Then pass the prompt to the LLM
    response = agent_executor.run(prompt)
    # ...and write it out to the screen
    st.write(response)