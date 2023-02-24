from rest_framework.serializers import ModelSerializer
from .models import Vis

class VisSerializer(ModelSerializer):
    class Meta:
        model = Vis
        fields = '__all__' 