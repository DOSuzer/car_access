import re

from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'uuid', 'brand', 'model', 'plate_number',
                  'owners_name', 'created_at', 'updated_at')
        read_only_fields = ('id', 'uuid', 'created_at', 'updated_at')

    def validate_plate_number(self, value):
        mask = r'^[АВЕКМНОРСТУХавекмнорстух]\d{3}(?<!000)[АВЕКМНОРСТУХавекмнорстух]{2}\d{2,3}$'
        if not re.fullmatch(mask, value):
            raise serializers.ValidationError('Введите правильный гос номер авто.')
        return value
