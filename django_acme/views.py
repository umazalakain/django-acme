from django.http import HttpResponse, Http404
from django.views.generic import View

from .settings import ACME_CHALLENGES


class AcmeChallenge(View):
    def get(self, request, *args, **kwargs):
        response = ACME_CHALLENGES.get(kwargs['token'])
        if response is None:
            raise Http404("Invalid token.")
        return HttpResponse(response)
