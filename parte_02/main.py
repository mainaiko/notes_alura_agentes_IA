import re, pathlib
from typing import List, Dict
from fabrica_de_corte import busca_similar as retriever
from Rag import document_chain

# Funções auxiliares de limpeza e formatação visual
def clean_text(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()

def extrair_trecho(texto: str, query: str, janela: int = 240) -> str:
    match = re.search(query, texto, re.IGNORECASE)
    if not match:
        return texto[:janela]

    meio = match.start()
    ini = max(0, meio - janela // 2)
    fim = min(len(texto), meio + janela // 2)

    if ini > 0:
        pos_espaco = texto.rfind(" ", 0, ini)
        if pos_espaco != -1:
            ini = pos_espaco + 1

    if fim < len(texto):
        pos_espaco = texto.find(" ", fim)
        if pos_espaco != -1:
            fim = pos_espaco

    return texto[ini:fim] # Retorna o recorte

def formatar_citacoes(docs_rel: List, query: str) -> List[Dict]:
    cites = []
    for doc in docs_rel:
        doc_limpo = clean_text(doc.page_content)
        nome_arquivo = pathlib.Path(doc.metadata.get("source", "N/A")).name
        cites.append({
            "fonte": nome_arquivo,
            "trecho": extrair_trecho(doc_limpo, query) + "..."
        })
    return cites[:3]

# --- A FUNÇÃO PRINCIPAL ---
def perguntar_politica_RAG(pergunta: str) -> Dict:
    # 1. Busca os documentos
    docs_relacionados = retriever.invoke(pergunta)

    if not docs_relacionados:
        return {"answer": "Não sei.", "contexto_encontrado": False}

    # 2. Pede a resposta ao LLM usando os documentos
    answer = document_chain.invoke({"input": pergunta, "context": docs_relacionados})

    # 3. Formata e retorna
    return {
        "answer": answer,
        "citacoes": formatar_citacoes(docs_relacionados, pergunta),
        "contexto_encontrado": True
    }


# Teste da função principal
pergunta_teste = "Qual é a política de reembolso para despesas de internet ao trabalhar de casa?"
resultado_teste = perguntar_politica_RAG(pergunta_teste)
print(f"Pergunta: {pergunta_teste}\nResposta: {resultado_teste['answer']}\n")