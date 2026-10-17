from django.urls import path

from portal import views

# ERRO ENCONTRADO: A variável app_name foi declarada como 'portal', mas não foi utilizada no arquivo urls.py.
# CORREÇÃO: A variável app_name deve ser declarada antes da lista urlpatterns para que o Django possa identificar corretamente o namespace do aplicativo.
app_name = 'portal'


#ERRO ENCONTRADO: Rota principal do aplicativo não foi definida corretamente. A rota principal deve ser definida como uma string vazia ('') para que o Django possa identificar corretamente a URL raiz do aplicativo.

# CORREÇÃO: Alterado a rota principal do aplicativo para uma string vazia ('') para que o Django possa identificar corretamente a URL raiz do aplicativo.
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
]