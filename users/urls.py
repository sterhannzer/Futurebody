from django.conf.urls import patterns, url
from django.contrib import admin
from users.views import UsersIndex, AddUser, UsersShow, UpdateUser

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', UsersIndex.as_view(), name='user'),
    url(r'^add/$', AddUser.as_view(), name='add'),
    url(r'^(?P<id>\d+)/$', UsersShow.as_view(), name='details'),
    url(r'^edit/(?P<id>\d+)/$', UpdateUser.as_view(), name='edit'),
)
