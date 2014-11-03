from django.conf.urls import patterns, url
from django.contrib import admin
from users.views import UsersIndex, AddUser

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', UsersIndex.as_view(), name='user'),
    url(r'^add/$', AddUser.as_view(), name='add'),
)
