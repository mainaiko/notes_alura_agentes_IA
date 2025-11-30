# imports necessarios
from pydantic import BaseModel, Field
from typing import Literal, List, Dict
# imports do langchain, usado para estruturar as mensagens enviadas ao modelo, mensagens do sistema e do usuario
from langchain_core.messages import SystemMessage, HumanMessage

from agente import llm
from promt import TRIAGEM_PROMPT

#classe para definir a estrutura do JSON de saída
class TriagemOutput(BaseModel): #estudar o basemodel melhor
    decisao: Literal["AUTO_RESOLVER", "PEDIR_INFO", "ABRIR_CHAMADO"]
    urgencia: Literal["BAIXA", "MEDIA", "ALTA"]
    campos_faltantes: List[str] = Field(default_factory=list)


# quem faz a triagem é o llm
# o modelo ira trabalhar em um padrao estruturado definido pela classe TriagemOutput
triagem_chain = llm.with_structured_output(TriagemOutput)

def triagem(mensagem: str) -> Dict:
    saida: TriagemOutput = triagem_chain.invoke([SystemMessage(content=TRIAGEM_PROMPT),
    HumanMessage(content=mensagem)])
    return saida.model_dump()  # converter o modelo pydantic para dicionario


#teste_mensagem = ["Posso reembolsar a internet que meu chefe usou para trabalhar de casa ontem?",
#"Quero mais 5 dias de trabalho remoto por mês, é possível?",
#"Meu notebook quebrou, preciso de um novo urgente, o que faço?"
#]
#
#for msg in teste_mensagem:
#    resultado = triagem(msg)
#    print(f"Mensagem: {msg}\nResultado da triagem: {resultado}\n")