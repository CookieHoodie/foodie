from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^owner-info/$', views.owner_info, name="owner-info"),
    url(r'^search/(?P<item_name>\w+)/$', views.search, name="search"),
]
