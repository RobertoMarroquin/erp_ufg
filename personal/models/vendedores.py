from django.db import models
from django.contrib.auth.models import User


class Vendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Vincula con el modelo User de Django
    numero_caja = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"  # Usa nombres del User
