from rest_framework.views import APIView
from rest_framework.response import Response
from customers.models import Client, Domain

class CrearTenant(APIView):
    def post(self, request):
        nombre = request.data['nombre']
        subdominio = request.data['subdominio']
        cliente = Client(schema_name=subdominio, name=nombre, paid_until='2025-12-31')
        cliente.save()
        Domain.objects.create(domain=f"{subdominio}.localhost", tenant=cliente)
        return Response({'status': 'ok'})
