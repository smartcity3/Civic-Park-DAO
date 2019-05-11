from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^campaigns/$', views.campaigns, name='campaigns'),
    # url(r'^campaigns/apriori$', views.)
]
