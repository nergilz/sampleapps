from django.urls import path
from sampleapi.views import ApplicationList

urlpatterns = [
    path('/', ApplicationList.as_view()),
]