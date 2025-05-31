from django.urls import path
from . import views

app_name = 'leo_stronda_app'  # Namespace para evitar conflitos

urlpatterns = [
    path('', views.home, name='home'),
    path('cursos/', views.cursos, name='cursos'),
    path('contatos/', views.contatos, name='contatos'),

]