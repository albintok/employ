from api.models import Employe
from rest_framework import serializers


class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employe
        fields="__all__"