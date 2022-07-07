from rest_framework.serializers import ModelSerializer
from Home.models import Student


class studentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
