from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

docs_pdf = [] #docs

#iterando sobre todos os arquivos pdf na pasta pdfs
for arquivo in Path("pdfs").glob("*.pdf"):
    try: 
        loader = PyMuPDFLoader(str(arquivo))
        docs_pdf.extend(loader.load())
    except Exception as e:
        print(f"Erro ao carregar {arquivo}: {e}")
        continue

# teste de quantos documentos foram carregados
# print (f"Total de documentos carregados: {len(docs_pdf)}")