from django.conf.urls import url

from .views import AcmeChallenge


urlpatterns = [
    url(r'^(?P<token>.+)/$', AcmeChallenge.as_view())
]
