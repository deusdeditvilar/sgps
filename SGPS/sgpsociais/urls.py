from django.urls import path
from .views import *

app_name = 'sgps'

urlpatterns = [
    path('', logon, name='logon'),
    path('logoff/', logoff, name='logoff'),
    path('home/', home, name='home'),
    path('cadastro_jovem/', cadastro_jovem, name='cadastro_jovem'),
    path('cadastro_crianca/', cadastro_crianca, name='cadastro_crianca'),
    path('cadastro_idoso/', cadastro_idoso, name='cadastro_idoso'),
    path('listar_jovem/', listar_jovem, name='listar_jovem'),
    path('listar_crianca/', listar_crianca, name='listar_crianca'),
    path('listar_idoso/', listar_idoso, name='listar_idoso'),
    path('suporte/', suporte, name='suporte'),
    path('preferencias/', preferencias, name='preferencias'),
]
