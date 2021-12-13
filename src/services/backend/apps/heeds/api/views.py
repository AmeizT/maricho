from rest_framework.utils import serializer_helpers
from apps.heeds.models import Heed
from rest_framework import viewsets, permissions
from .serializers import HeedSerializer

class HeedView(viewsets.ModelViewSet):
    queryset = Heed.objects.all()
    serializer_class = HeedSerializer
    permission_classes = [permissions.AllowAny]

