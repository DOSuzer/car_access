import graphene
from graphene.types.scalars import Scalar

from .models import Car
from .serializers import CarSerializer
from .types import CarType


class CarInput(graphene.InputObjectType):
    brand = graphene.String(required=True)
    model = graphene.String(required=True)
    plate_number = graphene.String(required=True)
    owners_name = graphene.String(required=True)


class ObjectField(Scalar):
    @staticmethod
    def serialize(dt):
        return dt


class CreateCarMutation(graphene.Mutation):
    class Arguments:
        input = CarInput(required=True)

    message = ObjectField()
    car = graphene.Field(CarType)

    @classmethod
    def mutate(cls, root, info, input=None):
        serializer = CarSerializer(data=input)
        if serializer.is_valid():
            obj = serializer.save()
            msg = 'success'
        else:
            msg = serializer.errors
            obj = None
        return cls(car=obj, message=msg)


class UpdateCarMutation(graphene.Mutation):

    class Arguments:
        id = graphene.Int(required=True)
        input = CarInput(required=True)

    message = ObjectField()
    car = graphene.Field(CarType)

    @classmethod
    def mutate(cls, root, info, id, input=None):
        car = Car.objects.get(pk=id)
        serializer = CarSerializer(car, data=input, partial=True)
        if serializer.is_valid():
            obj = serializer.save()
            msg = 'success'
        else:
            msg = serializer.errors
            obj = None
        return cls(car=obj, message=msg)


class DeleteCarMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID(required=True)

    message = ObjectField()

    @classmethod
    def mutate(cls, root, info, id, **kwargs):
        car = Car.objects.get(pk=id)
        car.delete()
        return cls(message='success')
