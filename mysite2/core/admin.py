from django.contrib import admin
from . models import updateberita1

# Register your models here.

class updateberita1Admin(admin.ModelAdmin):
    #list Display
    list_display = ['judul','isi','isi2','isi3','kategori','gambar','namapenulis','deskripsi','publikasi','gambarpenulis','tanggal','status']
    search_field = ['judul','kategori','nama']
    autocomplete_fields = ['kategori']

admin.site.register(updateberita1,updateberita1Admin)