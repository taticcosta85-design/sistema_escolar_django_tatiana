from django.contrib import admin

# ERRO ENCONTRADO: (from django.urls import path). O arquivo 'sistema/urls.py' não possui a importação da função 'include'. A função 'include' é necessária para que o sistema consiga se conectar com o app portal
# CORREÇÃO: Adicionamos a importação da função 'include' para que o sistema consiga se conectar com o app portal
from django.urls import include, path 

urlpatterns = [
    path('admin/', admin.site.urls),

# ERRO ENCONTRADO: path('cadastro'/, preciso mostrar a pagina cadastro.html). Isso causa um erro ao tentar acessar a página inicial do portal. Pois não há uma rota definida para a página inicial do portal.    
# CORREÇÃO: Sem prefixo, as urls do app ficam na raiz do site. Com prefixo, as urls do app ficam dentro de uma pasta com o nome do app.
    path('', include('portal.urls')),
]

