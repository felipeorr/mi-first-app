from django.conf.urls import patterns, url
from blog import views


urlpatterns = patterns('',
                     
						url(r'^$', views.prueba, name='index'),
						url(r'^metodo2/$', views.metodo2, name='metodo2'),
						url(r'^home/$', views.home, name='homess-list'),
                       )