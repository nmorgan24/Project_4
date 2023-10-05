from .models import Oilchange
from rest_framework import viewsets, permissions
from .serializers import OilchangeSerializer

class OilchangeViewSet(viewsets.ModelViewSet):
    ## queryset is a list of all Oilchange objects
    queryset = Oilchange.objects.all()
    # The serializer_class attribute is used to control which serializer class should be used for serializing and deserializing queryset and model instances.
    serializer_class = OilchangeSerializer
    # Set permission_classes to allow unrestricted access to the API.
    permission_classes = [permissions.AllowAny]