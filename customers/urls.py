from django.conf.urls import patterns, url
from django.contrib import admin
from customers.views import UsersIndex, AddUser, UsersShow, UpdateUser, UpdateNote

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', UsersIndex.as_view(), name='user'),
    url(r'^add/$', AddUser.as_view(), name='add'),
    url(r'^(?P<id>\d+)/$', UsersShow.as_view(), name='details'),
    url(r'^edit/(?P<id>\d+)/$', UpdateUser.as_view(), name='edit'),
    url(r'^edit_note/(?P<id>\d+)/$', UpdateNote.as_view(), name='edit_note'),
)
