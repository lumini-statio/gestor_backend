from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'meses', TaskView, 'meses')
router.register(r'gastos', GastoView, 'gastos')

urlpatterns = [
    path('/', include(router.urls)),
    path('/guardar_datos/', RegistroFinanzasView.as_view(), name='guardar_datos'),
    path('/guardar_gastos/', RegistroGastosView.as_view(), name='guardar_gastos'),
]