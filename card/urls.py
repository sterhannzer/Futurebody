from django.conf.urls import patterns, url
from django.contrib import admin
from card.views import AddCard, CardEdit, CardDelete
from customers.views import UsersIndex, AddUser, UsersShow

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^add/$', AddCard.as_view(), name='add'),
    url(r'^edit/(?P<id>\d+)/$', CardEdit.as_view(), name='edit'),
    url(r'^delete/(?P<id>\d+)/$', CardDelete.as_view(), name='delete'),
)
