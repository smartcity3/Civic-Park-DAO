from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('campaigns/', views.campaigns, name='campaigns'),
    url('campaigns/<int:id>/', views.campaigns, name='campaigns'),
    url('teams/', views.teams, name='teams'),
    url('teams/<int:id>/', views.teams, name='teams'),
]
