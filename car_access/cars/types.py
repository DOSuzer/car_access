from graphene_django.types import DjangoObjectType
from .models import Car


class CarType(DjangoObjectType):
    class Meta:
        model = Car
