from setuptools import setup

setup(
    name="django-acme",
    version="0.1",
    author="Unai Zalakain",
    author_email="unai@gisa-elkartea.org",
    description="Make Django answer ACME request",
    license="GPLv3",
    url="https://github.com/unaizalakain/django-acme/",

    packages=['django_acme'],
    install_requires=['django>=1.8'],
)
