from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Los Usuarios deben tener email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        user.set_password(password)
        user.save()
        
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email



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