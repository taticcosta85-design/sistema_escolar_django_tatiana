from django.shortcuts import render

def index(request):

    return render(
        request,
        'portal/index.html'
    )

# ERRO ENCONTRADO: O arquivo 'portal/views.py' não possui a view  'cadastro'. O arquivo 'urls.py' direciona para ela.
# CORREÇÃO: Criamos uma função chamada cadastro que retorna para o usuario a pagina de cadastro.
def cadastro(request):
    return render(request,'portal/cadastro.html')       

