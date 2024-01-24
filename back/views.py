from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Mes, Gasto
from .serializer import MesSerializer, GastoSerializer

class RegistroFinanzasView(APIView):
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

class GastoView(viewsets.ModelViewSet):
    serializer_class = GastoSerializer
    queryset = Gasto.objects.all()
