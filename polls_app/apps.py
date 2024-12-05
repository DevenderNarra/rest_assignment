from django.apps import AppConfig


class PollsAppAppConfig(AppConfig):
    name = "polls_app"

    def ready(self):
        from polls_app import signals # pylint: disable=unused-variable
