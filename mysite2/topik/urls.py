from django.urls import path
from . import views

app_name = 'topik'

urlpatterns = [
    path('isiberita/',views.topik, name = 'isiberita')
]