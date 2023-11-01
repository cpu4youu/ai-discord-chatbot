import os

import argparse

from langchain.llms import OpenAI

# The vectorstore we'll be using
from langchain.vectorstores import FAISS
from langchain.document_loaders import DirectoryLoader

# The LangChain component we'll use to get the documents
from langchain.chains import RetrievalQA

from langchain.text_splitter import RecursiveCharacterTextSplitter

# The easy document loader for text
from langchain.document_loaders import TextLoader

# The easy document loader for pdf
from langchain.document_loaders import PyPDFLoader

# The embedding engine that will convert our text to vectors
from langchain.embeddings.openai import OpenAIEmbeddings

from InstructorEmbedding import INSTUCTOR
from langchain.embeddings import HuggingFaceInstructEmbeddings

def getDocs(message):
  openai_api_key= os.getenv('OPENAI_API_KEY', 'sk-111111111111111111111111111111111111111111111111')
  os.environ["OPENAI_API_BASE"] = "http://192.168.1.14:5001/v1"
  llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

# ****************** ORIGINAL ******************
  # loader = PyPDFLoader("./Alien_Worlds_Technical_Blueprint.pdf")
  # pages = loader.load_and_split()
  # # print(pages[0])
  # text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=400)
  # docs = text_splitter.split_documents(pages)

  # load pdfs in folder
  loader = DirectoryLoader(
      './',
      glob='*.pdf',
      loader_cls=PyPDFLoader
  )
  documents = loader.load()

    # split all pdfs
  text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=1000,
      chunk_overlap=200
  )
  texts = text_splitter.split_documents(documents)

  # load  model
  instructor_embeddings = HuggingFaceInstructEmbeddings(model_name= "../airoboros-l2-70b-3.1.Q5_K_M.gguf", model_kwargs={"device":"cuda"})

  Embedding_store_path = "./"

  # **********************************EMBEDDING***************************************************
  # COMMENT THIS SECTION OUT AFTER INITIAL RUN ONCE FILE IS CREATED

  store_embeddings(texts, 
                 instructor_embeddings, 
                 sotre_name='instructEmbeddings', 
                 path=Embedding_store_path)

  db_instructEmbedd = load_embeddings(sotre_name='instructEmbeddings', 
                  path=Embedding_store_path)
  
  # **********************************EMBEDDING***************************************************

  db_instructEmbedd = FAISS.from_documents(texts, instructor_embeddings)

  retriever = db_instructEmbedd.as_retriever(search_kwargs={"k": 3})

  docs = retriever.get_relevant_documents(message)

  # qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())

  # Get your embeddings engine ready
  # embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
  
  
    #   load INSTRUCTOR_Transformer
    # max_seq_length  512

  # Embed your documents and combine with the raw text in a pseudo db. 
  # Note: This will make an API call to OpenAI
  # docsearch = FAISS.from_documents(docs, embeddings)

  # qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())
  print(docs.run(message))


def main():
    parser = argparse.ArgumentParser(description='Your program description here')
    parser.add_argument('message', help='The message for LLM processing')
    
    args = parser.parse_args()
    response = getDocs(args.message)
    #print("LLM Response:")
    print(response)

if __name__ == '__main__':
    main()