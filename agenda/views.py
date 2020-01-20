from django.shortcuts import render
from rest_framework import viewsets
from .models import Agenda
from .serializer import AgendaSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer   
