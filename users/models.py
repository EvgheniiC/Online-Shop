from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Avatar')
    # To see correct Product name in admin panel

    class Meta:
        db_table = 'user'
        verbose_name = 'Polzovatel'  # visual table name in admin panel
        verbose_name_plural = 'Polzovateli'  # visual table name in admin panel plural

    def __str__(self):
        return f'{self.username} '


