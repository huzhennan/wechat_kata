
from django.conf.urls import url
from . import views

app_name = 'kata'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^menu$', views.menu, name='menu')
]