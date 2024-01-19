from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'meses', TaskView, 'meses')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/guardar_datos/', RegistroFinanzasView.as_view(), name='guardar_datos'),
]