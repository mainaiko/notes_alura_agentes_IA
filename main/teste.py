#importacoes
from pydantic import BaseModel, Field
from typing import Literal, List, Dict

from main.agente import llm_teste
from main.promt import TRIAGEM_PROMPT

#classe para definir a estrutura do JSON de saída
class TriagemOutput(BaseModel):
    decisao: Literal["AUTO_RESOLVER", "PEDIR_INFO", "ABRIR_CHAMADO"]
    urgencia: Literal["BAIXA", "MEDIA", "ALTA"]
    campos_faltantes: List[str] = Field(default_factory=list)