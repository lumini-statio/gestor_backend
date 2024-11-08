from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import permission_classes
from .models import Mes, Gasto
from .serializers import MesSerializer, GastoSerializer, UserSerializer
from django.contrib.auth.models import User

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.data['password'])
            user.save()

            # Generar JWT para el nuevo usuario
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]

class RegistroFinanzasView(APIView):
    permission_classes = [TokenAuthentication]
    def post(self, request, *args, **kwargs):
        data = request.data

        try:

            registro_finanzas = Mes.objects.create(
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
    permission_classes = [TokenAuthentication]
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            mes_id = data.get('mes', None)
            if mes_id is not None:
                mes = Mes.objects.get(pk=mes_id)
                data['mes'] = mes
            registro_gastos = Gasto.objects.create(
                mes = data['mes'],
                nombre = data['nombre'],
                descripcion = data['descripcion'],
                cantidad = data['cantidad'],
            )
            return Response({'message': 'Datos guardados correctamente'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ActualizarMesView(APIView):
    permission_classes = [TokenAuthentication]
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

class TaskView(viewsets.ModelViewSet):
    permission_classes = [TokenAuthentication]
    serializer_class = MesSerializer
    queryset = Mes.objects.all()

class GastoView(viewsets.ModelViewSet):
    permission_classes = [TokenAuthentication]
    serializer_class = GastoSerializer
    queryset = Gasto.objects.all()
