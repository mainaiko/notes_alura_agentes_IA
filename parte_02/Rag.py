from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain

from parte_01.agente import llm # Este import já está correto se executarmos da raiz

prompt_rag = ChatPromptTemplate.from_template( #criando o prompt para o RAG
    [
    ("system",
     "Você é um Assistente de Políticas Internas (RH/IT) da empresa Carraro Desenvolvimento. "
     "Responda SOMENTE com base no contexto fornecido. "
     "Se não houver base suficiente, responda apenas 'Não sei'."),

    ("human", "Pergunta: {input}\n\nContexto:\n{context}")
]
)


# criando a cadeia de documentos com o prompt definido acima e unindo com o llm
document_chain = create_stuff_documents_chain(llm, prompt_rag)