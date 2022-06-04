from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from clinic.models import Client
from clinic.serializers import ClientSerializer



class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @action(detail=False, methods=['GET'], name='Get')
    def riskiest(self, request, *args, **kwargs):
        queryset = Client.objects.order_by('-score')[:10]

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

