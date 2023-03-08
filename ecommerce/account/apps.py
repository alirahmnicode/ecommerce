from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ecommerce.account"

    def ready(self) -> None:
        import ecommerce.account.signals
