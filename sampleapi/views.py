from django.shortcuts import render
from rest_framework import generics
from sampleapi.models import Application
from sampleapi.serializers import ApplicationSerializer


class ApplicationList(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer