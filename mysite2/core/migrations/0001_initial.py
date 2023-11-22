# Generated by Django 4.2.7 on 2023-11-17 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('News', '0007_alter_berita_kategoriid'),
    ]

    operations = [
        migrations.CreateModel(
            name='updateberita1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('deskripsi', models.CharField(max_length=255, null=True)),
                ('isi', models.CharField(max_length=9999)),
                ('isi2', models.CharField(max_length=9999, null=True)),
                ('isi3', models.CharField(max_length=9999, null=True)),
                ('kategoriID', models.IntegerField(null=True)),
                ('gambar', models.ImageField(upload_to='media')),
                ('namapenulis', models.CharField(max_length=255)),
                ('publikasi', models.CharField(max_length=255, null=True)),
                ('gambarpenulis', models.ImageField(null=True, upload_to='media')),
                ('tanggal', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(choices=[('publish', 'publish'), ('draft', 'draft')], max_length=200, null=True)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.kategori')),
            ],
        ),
    ]