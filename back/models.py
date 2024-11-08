from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Mes(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
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
        return f"{self.nombre} - {self.usuario.username}"

class Gasto(models.Model):
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20, default='')
    descripcion = models.TextField(max_length=100, null=True, blank=True, default='')
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - {self.usuario.username}"