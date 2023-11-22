from django.contrib import admin
from.models import berita,kategori,customuser

# Register your models here.

admin.site.register(customuser)

class kategoriadmin(admin.ModelAdmin):
    list_display=['namakategori']
    search_fields = ['namakategori']

admin.site.register(kategori,kategoriadmin)

class beritaAdmin(admin.ModelAdmin):
    #list Display
    list_display = ['judul','isi','isi2','isi3','kategori','gambar','namapenulis','deskripsi','publikasi','gambarpenulis','tanggal','status','kategoriID']
    search_field = ['judul','kategori','nama']
    autocomplete_fields = ['kategori']

admin.site.register(berita,beritaAdmin)

