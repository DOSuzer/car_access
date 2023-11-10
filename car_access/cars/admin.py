from django.contrib import admin

from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    model = Car

    readonly_fields = (
        'uuid',
        'created_at',
        'updated_at'
    )
    list_display = ('id', 'plate_number', 'brand', 'model', 'owners_name')
    list_filter = ('brand', 'model', 'owners_name')
    search_fields = ('plate_number', 'owners_name', )
    empty_value_display = '-пусто-'
    ordering = ('updated_at',)
