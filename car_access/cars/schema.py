import graphene

from graphene_django.types import ObjectType

from .models import Car
from .mutations import CreateCarMutation, UpdateCarMutation
from .types import CarType


class Query(ObjectType):
    cars = graphene.List(CarType)
    car = graphene.Field(CarType, car_id=graphene.Int())

    def resolve_cars(self, info, **kwargs) -> Car:
        return Car.objects.all().order_by('-updated_at')

    def resolve_car(self, info, car_id: int) -> Car:
        return Car.objects.get(pk=car_id)


class Mutation(ObjectType):
    create_car = graphene.Field(CreateCarMutation)
    update_car = graphene.Field(UpdateCarMutation)


schema = graphene.Schema(query=Query, mutation=Mutation)
