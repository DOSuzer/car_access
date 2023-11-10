from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):

    uuid = models.UUIDField(editable=False, default=uuid4(), unique=True)
    created_at = models.DateTimeField(verbose_name='Создан', editable=False)
    updated_at = models.DateTimeField(verbose_name='Обновлен', )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    def save(self, *args, **kwargs):
        '''При сохранение обновляем updated_at.'''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
