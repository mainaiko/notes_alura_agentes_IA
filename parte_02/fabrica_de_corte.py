from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings #recurso do gemini
from langchain_community.vectorstores import FAISS

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dados_modelo import docs_pdf
from parte_01.agente import api_key

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30) #ferramenta para dividir textos grandes em pedaços menores
chunks = splitter.split_documents(docs_pdf) #armazenando os pedaços na variavel chunks

# modelo que sera usado para transformar os pedacos de texto em vetores
vetor = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)

# estoque de vetores para consulta de similaridade
estoque_de_vetores = FAISS.from_documents(chunks, vetor) #estudar melhor o FAISS
    
# configurando a busca por similaridade utilizando o estoque de vetores
busca_similar = estoque_de_vetores.as_retriever(search_type="similarity_score_threshold", search_kwargs={"score_threshold":0.3,"k":4})