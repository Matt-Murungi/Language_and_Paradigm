from django.shortcuts import render
from rest_framework import viewsets
from .models import LanguageModel
from .serializer import LanguageSerializer

class LanguageView(viewsets.ModelViewSet):
  queryset = LanguageModel.objects.all()
  serializer_class = LanguageSerializer