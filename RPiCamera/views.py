from rest_framework import viewsets
from .serializers import capture_serializer
from .models import rpi_parameter
from rest_framework import permissions

class capture_viewset(viewsets.ModelViewSet):
    queryset = rpi_parameter.objects.all()
    serializer_class = capture_serializer
    permission_classes = (permissions.IsAuthenticated, )

    