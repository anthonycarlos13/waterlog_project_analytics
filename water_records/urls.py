from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^groundwater/$', views.groundwater, name='groundwater'),
    # url(r'^recycledwater/$', views.recycledwater, name='recycledwater'),
    # url(r'^runoffwater/$', views.runoffwater, name='runoffwater'),
    # url(r'^importedwater/$', views.importedwater, name='imported'),
]
