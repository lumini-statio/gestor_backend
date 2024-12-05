from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

router = routers.DefaultRouter()
router.register(r'meses', MesesView, 'meses')
router.register(r'gastos', GastoView, 'gastos')

urlpatterns = [
    path('', include(router.urls)),
    path('guardar_datos/', RegistroFinanzasView.as_view(), name='guardar_datos'),
    path('guardar_gastos/', RegistroGastosView.as_view(), name='guardar_gastos'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('api/token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
]