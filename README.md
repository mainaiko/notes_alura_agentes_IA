# notes_alura_agentes_IA
Aulas imersao alura agentes ia (não tive tempo de terminar na semana da imersão mas tomei liberdade para destrinchar o codigo eu mesma)

Visão geral do codigo
1-> Criar um triador para definir a intenção do usuario
2-> Se a intenção se encaixar em "autoresolver" utilizar o sistema RAG para procurar a resposta nos pdfs
3-> Se a inteção for outra ele abre um chamado ou pede mais informações


Ja havia visto algumas coisas sobre agentes e llm e estava a procura de algum projeto que me ensinasse na base como funciona o assunto, e nessas aulas da alura obtive bastante conhecimento, infelizmente não consegui codar e assistir pois estava na semana de provas da faculdade, então decidi ver as aulas e codifiquei eu mesma sozinha usando como base o codigo disponibilizado na aula.

1- Começamos instanciando o agente utilizando uma apikey do proprio google, apos isso fazer um teste, tomei a liberdade de alterar algumas coisas como uma condicional que verifica se a chave api existe mesmo. Separei o codigo em pastas, por aula e por função de codigo.
2- Peguei a variavel triagem_prompt na aula para dar continuidade.
3- Criei um arquivo para fazer a triagem do agente utilizando as blibliotecas: pydantic para organizar os dados e langchain para definir a mensagem do sistema e a mensagem do usuario.

