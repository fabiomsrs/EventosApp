from django.conf.urls import url,include
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$',views.index, name='login'),
	url(r'^$',views.logout, name='logout'),
	url(r'^home/$',views.home, name='home'),	
	url(r'^cadastroUsuario/$',views.cadastro_usuario, name='cadastro_usuario'),

	#urls de outras apps
	url(r'^evento/',include('core.urls', namespace='evento')),
    url(r'^inscricao/',include('inscricao.urls', namespace='inscricao')),  		
    url(r'^cupom/',include('inscricao.urls', namespace='cupom')), 
    url(r'^comum/',include('comum.urls', namespace='tag')),      
]
