import os


def get_challenges(env):
    cs = (v for k, v in env.items() if k.startswith('ACME_CHALLENGE'))
    return {c.split('.')[0]: c for c in cs}

ACME_CHALLENGES = get_challenges(os.environ)
