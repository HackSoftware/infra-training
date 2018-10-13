from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "infra_training.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
