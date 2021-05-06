import factory
from factory.django import DjangoModelFactory
from .models import Organization


class OrganizationFactory(DjangoModelFactory):
    """
    An organization factory class
    """
    name = factory.Faker('company')
    code = factory.Faker('isbn10')

    class Meta:
        model = Organization
        django_get_or_create = ('name',)
