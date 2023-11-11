import graphene

from graphene_django.types import ObjectType

from .models import Car
from .mutations import CreateCarMutation, DeleteCarMutation, UpdateCarMutation
from .types import CarType


class Query(ObjectType):
    cars = graphene.List(CarType)
    car = graphene.Field(CarType, car_id=graphene.Int())

    def resolve_cars(self, info, **kwargs) -> Car:
        return Car.objects.all().order_by('-updated_at')

    def resolve_car(self, info, car_id: int) -> Car:
        return Car.objects.get(pk=car_id)


class Mutation(graphene.ObjectType):
    create_car = CreateCarMutation.Field()
    update_car = UpdateCarMutation.Field()
    delete_car = DeleteCarMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
