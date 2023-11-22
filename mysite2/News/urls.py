from django.urls import path
from . import views

app_name = 'News'

urlpatterns = [
    path('all/' , views.all, name='all'),
    path('trending/',views.trending, name='trending'),
    path('sport/',views.sport, name='sport'),
    path('ekonomi/',views.ekonomi, name='ekonomi'),
    path('kesehatan/',views.kesehatan, name='kesehtan'),
    path('topik/<int:id>',views.topik, name='topik'),
]