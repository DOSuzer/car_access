from uuid import uuid4

from django.db import models
from django.utils import timezone


class Car(models.Model):

    uuid = models.UUIDField(editable=False, unique=True)
    brand = models.CharField(max_length=20, verbose_name='Марка')
    model = models.CharField(max_length=20, verbose_name='Модель')
    plate_number = models.CharField(max_length=9,
                                    verbose_name='Гос номер',
                                    unique=True)
    owners_name = models.CharField(max_length=70, verbose_name='ФИО владельца')
    created_at = models.DateTimeField(verbose_name='Создан', editable=False)
    updated_at = models.DateTimeField(verbose_name='Обновлен', )

    class Meta:
        ordering = ['updated_at']
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def save(self, *args, **kwargs):
        '''При сохранение обновляем updated_at.'''
        if not self.uuid:
            self.uuid = uuid4()
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Car, self).save(*args, **kwargs)

    def __str__(self):
        return self.plate_number
