# imports necessarios
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

#carregar a chave da API do arquivo .env
load_dotenv()
api_key = os.getenv("MINHA_API_KEY") #google_api_key

# verificar se a chave foi carregada corretamente
#if api_key is None:
#    raise ValueError("A variável de ambiente 'MINHA_API_KEY' não está definida.")

# configurar o modelo de linguagem
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0, #para respostas mais precisas
    api_key=api_key
    )

#teste do modelo
#resposta_1 = llm_teste.invoke("Quem foi Albert Einstein?")
#print(resposta_1.content)