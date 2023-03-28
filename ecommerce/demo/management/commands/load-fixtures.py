from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command("makemigrations")
        call_command("migrate")
        print("catrgory started")
        call_command("loaddata", "db_category_fixture.json")
        print("product started")
        call_command("loaddata", "db_product_fixture.json")
        print("catrgory product started")
        call_command("loaddata", "db_category_product_fixture.json")
        print("brand started")
        call_command("loaddata", "db_brand_fixture.json")
        print("product inventory started")
        call_command("loaddata", "new_product_inventory.json")
        print("media started")
        call_command("loaddata", "db_media_fixture.json")
        print("stock started")
        call_command("loaddata", "new_stock.json")
