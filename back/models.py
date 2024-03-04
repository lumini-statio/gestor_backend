from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class Mes(models.Model):
    nombre = models.CharField(max_length=20)
    sueldo_total = models.DecimalField(max_digits=10, decimal_places=2)
    resultado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    gasto_gas = models.DecimalField(max_digits=10, decimal_places=2)
    gasto_luz = models.DecimalField(max_digits=10, decimal_places=2)
    gasto_agua = models.DecimalField(max_digits=10, decimal_places=2)
    gasto_comida = models.DecimalField(max_digits=10, decimal_places=2)
    resto = models.DecimalField(max_digits=10, decimal_places=2)
    expensas = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)
    alquiler = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    wifi = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)

    def __str__(self):
        return self.nombre
    

class Gasto(models.Model):
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20, default='')
    descripcion = models.TextField(max_length=100, null=True, blank=True, default='')
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre