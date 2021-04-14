from rest_framework import serializers
from .models import rpi_parameter


class capture_serializer (serializers.ModelSerializer):
    class Meta:
        model = rpi_parameter
        fields = ['save_folder', "num_of_capture", "width", "height"]