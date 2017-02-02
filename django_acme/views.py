import os

from django.http import HttpResponse, Http404
from django.utils.decorators import classonlymethod
from django.views.generic import View


def get_challenges(env):
    cs = (v for k, v in env.items() if k.startswith('ACME_CHALLENGE'))
    return {c.split('.')[0]: c for c in cs}


class AcmeChallenge(View):
    ACME_CHALLENGES = {}

    @classonlymethod
    def as_view(cls, **initkwargs):
        initkwargs['ACME_CHALLENGES'] = get_challenges(os.environ)
        return super().as_view(**initkwargs)

    def get(self, request, *args, **kwargs):
        response = get_challenges(os.environ).get(kwargs['token'])
        if response is None:
            raise Http404("Invalid token.")
        return HttpResponse(response)
