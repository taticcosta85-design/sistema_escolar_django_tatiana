# Nome completo: Tatiana Christina Costa de Oliveira

# Descrição do projeto:

Foi desenvolvido um Projeto de um Sistema Escolar utilizando Framework Django para cadastro de informações de Professores, Alunos e Aulas.

# O cadastro do Professor deve conter as seguintes informações:

1. Nome
2. Sobrenome
3. Email
4. Data da criação do cadastro
5. Registro do professor
6. Disciplina que o professor oferece
7. Atividade - se o professor está ativo ou não no sistema
8. Observação - campo opcional para escrita de uma observação
9. Imagem - campo opcional para inserção de imagem do professor no sistema

# O cadastro do Aluno deve conter as seguintes informações:

1. Nome
2. Sobrenome
3. Email
4. Telefone
5. Matrícula
6. Data de criação do cadastro
7. Observação - campo opcional para escrita de uma observação
8. Atividade - se o aluno está ativo ou não no sistema
9. Imagem - campo opcional para inserção de imagem do aluno no sistema

# O cadastro das Aulas deve conter as seguintes informações:

1. Aluno_id
2. Professor_id
3. Horário
4. Observação
5. Status

---

# ERROS

# --> Arquivo: models.py (02 erros)

O arquivo models.py geralmente contem:

- As ferramentas importadas do Django que são uteis para o nosso projeto - "os imports"
- As classes com atributos e seus tipos
- Os métodos (ações)

# ERRO ENCONTRADO (01):

Linha 04 - Ausência da importação da ferramenta que fornece data/ hora com fuso horário correto.

# CORREÇÃO (01):

from django.utils import timezone
((Sem essa parte do código, o Python não vai saber interpretar a instrução presente no campo "criação_data"))

# ERRO ENCONTRADO (02):

Linha 15: - registro = models.CharField(max_length=10)
Linha 31 - matricula = models.IntegerField()

# CORREÇÃO (02):

Linha 15 - registro = models.CharField(max_length=10, unique=True)
Linha 31 - matricula = models.IntegerField(unique=True)
((Para garantir que não existam registros duplicados, os atributos "matrícula" (na classe Aluno) e "registro" (na classe professor) devem possuir regra de restrição.))

# ERRO ENCONTRADO :

O campo "imagem" (linhas 21 e 39) depende da instalação da biblioteca Pillow no computador. Se a biblioteca Pillow não estiver instalada, aparece uma mensagem de erro no terminal e o sistema trava.

# CORREÇÃO:

Antes de rodar o servidor, devemos instalar a biblioteca Pillow
escrevendo no terminal o comando: pip install django Pillow

---

# --> Arquivo: admin.py (01 erro)

O Django vem com um painel administrativo pronto. Para que os nossos models apareçam la precisamos importar o módulo pronto do Django, importar os models e registrá-los no arquivo.

# ERRO ENCONTRADO (03):

Linha 8 - list_display = ('id', 'nome', 'email', 'telefone', 'especialidade', 'ativo',) - Não existe o campo "especialidade", dentro da Classe Professor, no arquivo models.py. Se deixar assim, o Django vai procurar por "especialidade" e vai apresentar uma mensagem de erro no servidor.

# CORREÇÃO (03):

list_display = ('id', 'nome', 'email', 'telefone', 'disciplina', 'ativo',) - O "list display" define quais colunas devem aparecer no nosso Portal Administrativo. Todos os campos, atributos ou métodos listados devem existir no models.py. Por isso, trocamos o campo "especialidade" pelo campo "disciplina" que está presente dentro da Classe Professor.

---

# --> Arquivo: settings.py (01 erro)

O arquivo settings.py é o arquivo de configurações do Django.
Nele definimos os apps instalados, onde ficam os templates, como funciona o banco de dados, idioma, fuso horário e etc.

# ERRO ENCONTRADO (04):

Ausência do app "portal" na lista de apps instalados. Sem ela escrita nessa lista, para o Django, é como se essa pasta ficasse invisível para o sistema. É uma espécie de registro do app.

# CORREÇÃO (04):

'portal',
Embora a pasta portal exista fisicamente, você precisa dizer ao Django que ela está habilitada e que ele deve consultá-la colocando ela na lista de apps instalados.

---

# --> Arquivo: views.py (01 erro)

A view é um arquivo que contém uma função ou classe Python responsável por executar uma ação.
Ela recebe uma solicitação -> consulta infos/prepara uma página html -> devolve uma resposta

# ERRO ENCONTRADO (05):

O arquivo 'portal/views.py' não possui a view 'cadastro'. O arquivo 'urls.py' direciona para ela. Ao iniciar, o Django verifica as rotas do projeto. Quando encontra uma referência a uma função inexistente, ocorre um erro, impedindo o carregamento correto das URLs e a inicialização do servidor.

# CORREÇÃO (05):

def cadastro(request):
return render(request,'templates/portal/cadastro.html')
Criamos uma função chamada 'cadastro' que retorna para o usuário a página de cadastro.

---

# --> Arquivo : urls.py/sistema (01 erro)

O sistema de URLs é o mapa de roteamento. Ele diz ao Django qual view deve ser chamada quando o usuário digitar uma determinada url no navegador.

# ERRO ENCONTRADO(06):

Linha 04 - (from django.urls import path)
O arquivo 'urls.py' não possui a importação da função 'include'. A função 'include' é necessária para que o sistema consiga redirecionar para a página de cadastro.

Linha 10 - path('cadastro'/, preciso mostrar a pagina cadastro.html)
O arquivo 'urls.py' não possui a importação da função 'include'. A função 'include' é necessária para que o sistema consiga redirecionar para a página de cadastro.  
Isso causa um erro ao tentar acessar a página inicial do portal. Pois não há uma rota definida para a página inicial do portal.

# CORREÇÃO (06):

Linha 04 - from django.urls import include, path
Adicionamos a importação da função 'include' para que o sistema consiga redirecionar para a página de cadastro.

Linha 10 - path('', include('portal.urls')),
Sem prefixo, as urls do app ficam na raiz do site. Com prefixo, as urls do app ficam dentro de uma pasta com o nome do app.

---

# --> Arquivo portal/urls.py (01 erro):

# ERRO ENCONTRADO (07):

O arquivo 'views.py' não possui a views do cadastro. O arquivo 'urls.py' direciona para ela.
Ao iniciar, o Django verifica as rotas do projeto. Quando encontra uma referência a uma função inexistente, ocorre um erro, impedindo o carregamento correto das URLs e a inicialização do servidor.

# CORREÇÃO (05):

def cadastro(request):
return render(request,'templates/portal/cadastro.html')
Criamos uma função chamada 'cadastro' que retorna para o usuário a página de cadastro.

---

# --> Arquivo: sistema/urls.py (01 erro)

O sistema de URLs é o mapa de roteamento. Ele diz ao Django qual view deve ser chamada quando o usuário digitar uma determinada "url" no navegador.

# ERRO ENCONTRADO (06):

Linha 04 - (from django.urls import path)
O arquivo 'urls.py' não possui a importação da função 'include'. A função 'include' é necessária para que o sistema consiga redirecionar para a página de cadastro.

Linha 10 - path('cadastro'/, preciso mostrar a pagina cadastro.html)
O arquivo 'urls.py' não possui a importação da função 'include'. A função 'include' é necessária para que o sistema consiga redirecionar para a página de cadastro.  
Isso causa um erro ao tentar acessar a página inicial do portal. Pois não há uma rota definida para a página inicial do portal.

# CORREÇÃO (06):

from django.urls import include, path
path('', include('portal.urls')),
Adicionamos a importação da função 'include' para que o sistema consiga redirecionar para a página de cadastro.
Sem prefixo, as urls do app ficam na raiz do site. Com prefixo, as urls do app ficam dentro de uma pasta com o nome do app.

---

# --> Arquivo: portal/urls.py (01 erro)

# ERRO ENCONTRADO (07):

Linha 07 - Ausência do namespace do aplicativo (app_name = 'portal').

Linha 11 e 12 - Rota principal configurada incorretamente com o caminho 'index/' em vez da raiz vazia ('').
Falta de identificadores (name='index' e name='cadastro') nas rotas, impedindo o uso de referências nomeadas nos templates.

# CORREÇÃO (07):

Linha 07 - Adicionada a variável app_name = 'portal' para registrar o namespace do app.

Linha 11 e 12 - Alterado o caminho da view inicial ('') para responder diretamente à raiz.
Incluídos os parâmetros name='index' e name='cadastro' nas funções path().

---

# Instruções de como rodar o projeto localmente:

1. Instalar as 2 bibliotecas necessárias (django e pillow):
   python pip install django pillow

2. Aplicar as migrações necessárias ao banco de dados:
   python manage.py migrate

3. Iniciar o servidor Django:
   python manage.py runserver
