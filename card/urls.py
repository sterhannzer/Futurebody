from django.conf.urls import patterns, url
from django.contrib import admin
from card.views import AddCard, CardEdit, CardDelete, AddEntranceCard, EntranceCardDelete, EntranceCardEdit
from customers.views import UsersIndex, AddUser, UsersShow


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^add/$', AddCard.as_view(), name='add'),
    url(r'^add_entrance/$', AddEntranceCard.as_view(), name='add_entrance'),
    url(r'^edit/(?P<id>\d+)/$', CardEdit.as_view(), name='edit'),
    url(r'^add_entrance/(?P<id>\d+)/$', EntranceCardEdit.as_view(), name='edit_entrance'),
    url(r'^delete/(?P<id>\d+)/$', CardDelete.as_view(), name='delete'),
    url(r'^delete_entrance/(?P<id>\d+)/$', EntranceCardDelete.as_view(), name='delete_entrance'),
)
