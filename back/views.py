from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Mes
from .serializer import MesSerializer

class RegistroFinanzasView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

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

class ActualizarMesView(APIView):
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
    serializer_class = MesSerializer
    queryset = Mes.objects.all()
