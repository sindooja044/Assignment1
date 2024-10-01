from django.apps import AppConfig


class ProjectappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projectapp'


class YourAppConfig(AppConfig):
    name = 'your_app'

    def ready(self):
        import projectapp.signals

