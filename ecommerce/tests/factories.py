import factory
import pytest
from ecommerce.inventory import models
from faker import Faker
from pytest_factoryboy import register

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = fake.lexify(text="cat_name_??????")
    slug = fake.lexify(text="cat_slug_??????")


register(CategoryFactory)
