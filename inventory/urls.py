from django.conf.urls import url
from django.urls import include, path
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_book$',add_book, name='add_book'),
    url(r'^edit_book/(?P<pk>\d+)$',edit_book, name='edit_book'),
    url(r'^delete_book/(?P<pk>\d+)$',delete_book, name='delete_book'),
    path('search_book',search_book, name='search_book'),
    url(r'^about$',about,name='about')
]