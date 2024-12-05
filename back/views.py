from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Mes, Gasto
from rest_framework_simplejwt.exceptions import InvalidToken
from .serializers import MesSerializer, GastoSerializer, UserSerializer
from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from gestion_api import settings

class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh_token')
        
        if not refresh_token:
            return Response({"error": "No refresh token provided"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            request.data['refresh'] = refresh_token
            response = super().post(request, *args, **kwargs)
            
            if response.status_code == 200:
                access_token = response.data['access']
                response.set_cookie(
                    'access_token',
                    access_token,
                    httponly=True,
                    secure=False if settings.DEBUG else True,
                    samesite='Lax'
                )
                del response.data['access']

            return response
        
        except InvalidToken:
            return Response({"error": "Invalid refresh token"}, status=status.HTTP_401_UNAUTHORIZED)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        email = attrs.get('username')
        if not email:
            raise serializers.ValidationError("El correo electrónico es obligatorio.")
        return super().validate(attrs)

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            access_token = response.data['access']
            refresh_token = response.data['refresh']
            
            # Configura las cookies
            response.set_cookie(
                'access_token', 
                access_token, 
                httponly=True, 
                secure=False if settings.DEBUG else True,
                samesite='Lax'
            )
            response.set_cookie(
                'refresh_token', 
                refresh_token, 
                httponly=True, 
                secure=False if settings.DEBUG else True,
                samesite='Lax'
            )
            
            del response.data['access']
            del response.data['refresh']
        
        return response

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario registrado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistroFinanzasView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def post(self, request, *args, **kwargs):
        data = request.data
        usuario = request.user
        try:
            registro_finanzas = Mes.objects.create(
                usuario=usuario,
                sueldo_total=data['sueldoTotal'],
                resultado=data['resultado'],
                gasto_gas=data['gas'],
                gasto_luz=data['luz'],
                gasto_agua=data['agua'],
                gasto_comida=data['minimoComida'],
                resto=data['resto'],
                nombre=data['nombre'],
                expensas=data['expensas'],
                alquiler=data['alquiler'],
                wifi=data['wifi']
            )
            return Response({'message': 'Datos guardados correctamente'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RegistroGastosView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def post(self, request, *args, **kwargs):
        data = request.data
        usuario = request.user
        try:
            mes = Mes.objects.get(pk=data['mes'], usuario=usuario)
            registro_gastos = Gasto.objects.create(
                mes=mes,
                usuario=usuario,
                nombre=data['nombre'],
                descripcion=data['descripcion'],
                cantidad=data['cantidad'],
            )
            return Response({'message': 'Datos guardados correctamente'}, status=status.HTTP_201_CREATED)
        except Mes.DoesNotExist:
            return Response({'error': 'El mes no existe o no pertenece al usuario'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ActualizarMesView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def put(self, request, pk, *args, **kwargs):
        try:
            mes = Mes.objects.get(pk=pk)
            serializer = MesSerializer(mes, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Mes.DoesNotExist:
            return Response({'message': 'El mes no existe'}, status=status.HTTP_404_NOT_FOUND)

class MesesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = MesSerializer
    queryset = Mes.objects.all().order_by('-id')

class GastoView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = GastoSerializer
    queryset = Gasto.objects.all().order_by('-id')
