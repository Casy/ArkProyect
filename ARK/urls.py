from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
  	url(r'^$', 'arkapp.views.inicio'),
  	url(r'^inicio/', 'arkapp.views.inicio_busqueda'), 
  	url(r'^busqueda-avanzada', 'arkapp.views.busqueda_avanzada'), 	
  	url(r'^resultados-busqueda', 'arkapp.views.resultados_busqueda'), 	  	
    url(r'^publicar-documento/', 'arkapp.views.publicar_documento'),
    url(r'^escribir-resena/', 'arkapp.views.publicar_documento'),
    url(r'^mis-referencias/', 'arkapp.views.mis_referencias'),
    url(r'^faq/', 'arkapp.views.faq'),
    url(r'^terminos-y-politicas/', 'arkapp.views.terminos_y_politicas'),
    url(r'^mis-valoraciones/', 'arkapp.views.mis_valoraciones'),
    url(r'^mis-publicaciones/', 'arkapp.views.mis_publicaciones'),
    url(r'^mis-referencias/', 'arkapp.views.mis_referencias'),
    url(r'^mi-perfil/', 'arkapp.views.mi_perfil'),
    url(r'^mis-estadisticas/', 'arkapp.views.mis_estadisticas'),
    url(r'^cerrar-sesion/', 'arkapp.views.cerrar_sesion'),
    url(r'^consola-usuarios/', 'arkapp.views.consola_usuarios'),
    url(r'^modificar-datos-usuario/', 'arkapp.views.modificar_datos_usuario'),
    url(r'^ver-publicacion/', 'arkapp.views.ver_publicacion'),
]
