import factory.django
from factory.fuzzy import FuzzyDecimal

from product.models import Product, Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('name')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    category = factory.SubFactory(CategoryFactory)
    name = factory.Faker('name')
    price = FuzzyDecimal(0.5, 42.7, 2)
    image = 'products_imgs/pinkRose.jpeg'
