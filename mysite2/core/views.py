from django.shortcuts import render, get_object_or_404
from . import models
from News import models as mdl


# Create your views here.
def index(request):
    berita = models.updateberita1.objects.filter(status='publish')
    berita2= mdl.berita.objects.filter(status='publish')
    kategori = mdl.kategori.objects.all()
    catID = 1
    if catID :
        berita2 = mdl.berita.objects.filter(kategori = catID)
    else :
        berita2 = mdl.berita.objects.filter(status='publish')
    
    context = {'updates' : berita, 'beritas' : berita2, 'kategori' : kategori}
    return render(request, 'core/index.html', context)

def isi(request,id):
    berita = get_object_or_404(models.updateberita1,pk=id)
    berita2 = models.updateberita1.objects.filter(status='publish')
    context = {'beritas' : berita, 'beritass' : berita2}
    return render(request, 'core/index.html', context)

