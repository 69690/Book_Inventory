from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^display_books$',index, name='display_books'),
    url(r'^add_book$',add_book, name='add_book')
]