from django.apps import AppConfig


class TestAppAppConfig(AppConfig):
    name = "test_app"

    def ready(self):
        from test_app import signals # pylint: disable=unused-variable
