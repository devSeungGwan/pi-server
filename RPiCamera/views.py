from rest_framework import viewsets
from .serializers import rpi_capture_serializer
from .models import rpi_parameter
from rest_framework import permissions

class rpi_capture_view(viewsets.ModelViewSet):
    queryset = rpi_parameter.objects.all()
    serializer_class = rpi_capture_serializer
    permission_classes = (permissions.IsAuthenticated, )