from django.shortcuts import render
from News import models as mdl

# Create your views here.
def topik (request):
    berita = mdl.models.objects.get()
    context = {'berita' : berita}
    return render(request, 'berita/isiberita.html')

