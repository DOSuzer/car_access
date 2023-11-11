import graphene
from graphene_django.rest_framework.mutation import SerializerMutation

from .models import Car
from .types import CarType


class CarInput(graphene.InputObjectType):
    brand = graphene.String(required=True)
    model = graphene.String(required=True)
    plate_number = graphene.String(required=True)
    owners_name = graphene.String(required=True)


class CreateCarMutation(graphene.Mutation):
    class Arguments:
        input = CarInput(required=True)

    car = graphene.Field(CarType)

    def mutate(cls, info, input=None):
        new_car = Car(
            brand=input.brand,
            model=input.model,
            plate_number=input.plate_number,
            owners_name=input.owners_name,
        )
        new_car.save()
        return CreateCarMutation(car=new_car)


class UpdateCarMutation(graphene.Mutation):

    class Arguments:
        id = graphene.Int(required=True)
        input = CarInput(required=True)

    ok = graphene.Boolean()
    car = graphene.Field(CarType)

    def mutate(cls, info, id, input=None):
        ok = False
        car = Car.objects.get(pk=id)
        if car:
            ok = True
            car.brand = input.brand
            car.model = input.model
            car.plate_number = input.plate_number
            car.owners_name = input.owners_name
            car.save()
            return UpdateCarMutation(ok=ok, car=car)
        return UpdateCarMutation(ok=ok, car=None)
