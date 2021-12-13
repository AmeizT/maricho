from apps.heeds.models import Heed
from rest_framework import serializers

class HeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heed
        fields = '__all__'