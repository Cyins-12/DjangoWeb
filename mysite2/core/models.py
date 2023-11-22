from django.db import models
from News import models as mdl


# Create your models here.
class updateberita1(models.Model):
    STATUS =('publish','publish'),('draft','draft')

    judul = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255,null=True)
    isi = models.CharField(max_length=9999)
    isi2 = models.CharField(max_length=9999,null=True)
    isi3 = models.CharField(max_length=9999,null=True)
    kategori = models.ForeignKey(mdl.kategori ,on_delete=models.CASCADE)
    gambar = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100)
    namapenulis = models.CharField(max_length =255)
    publikasi = models.CharField(max_length =255, null=True)
    gambarpenulis = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100,null=True)
    tanggal = models.CharField(max_length =255,null=True)
    status = models.CharField(choices=STATUS, max_length=200, null=True)