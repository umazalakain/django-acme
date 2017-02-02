Just a tiny view that exposes `ACME_CHALLENGE*` environment variables.

The environment is read at view construction. Multiple ACME challenges can be
declared:

    export ACME_CHALLENGE_0="foo_token.foo_secret"
    export ACME_CHALLENGE_C="bar_token.bar_secret"

Simply add the endpoint by including the URL pattern definitions:

    urlpatterns = [
        …
        url(r'^.well-known/acme-challenge/', include('django_acme.urls')),
        …
    ]
