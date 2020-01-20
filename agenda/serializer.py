from rest_framework import serializers
from .models import Agenda

class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agenda
        fields = ['nome', 'telefone', 'endereco', 'email']