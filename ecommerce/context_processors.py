from ecommerce.inventory.models import Category


def site_settings(request):
    categories = Category.objects.all()
    return {"categories": categories}
