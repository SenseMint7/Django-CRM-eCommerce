from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class SuitConfig(DjangoSuitConfig):
    """
    django-suit setting
    """
    layout = 'horizontal'


class UserConfig(AppConfig):
    name = 'user'
