from django.db import models


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
        return {self.nombre}
