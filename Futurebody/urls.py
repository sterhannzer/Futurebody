from django.conf.urls import patterns, include, url
from django.contrib import admin

from Futurebody.views import Home

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^users/', include('customers.urls', namespace='users_app')),
    url(r'^card/', include('card.urls', namespace='cards_app')),
    url(r'^admin/', include(admin.site.urls)),
)
