Just a tiny view that exposes `ACME_CHALLENGE*` environment variables.

Multiple ACME challenges can be declared:

    export ACME_CHALLENGE_0="foo_token.foo_secret"
    export ACME_CHALLENGE_C="bar_token.bar_secret"

The environment is read at view construction time, when you add the enpoint by
including the URL definitions:

    urlpatterns = [
        …
        url(r'^.well-known/acme-challenge/', include('django_acme.urls')),
        …
    ]

**WARNING**: You shouldn't be doing this with Django, but with your web server.
