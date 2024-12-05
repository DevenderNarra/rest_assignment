from django.apps import AppConfig


class TestApp1AppConfig(AppConfig):
    name = "test_app1"

    def ready(self):
        from test_app1 import signals # pylint: disable=unused-variable
