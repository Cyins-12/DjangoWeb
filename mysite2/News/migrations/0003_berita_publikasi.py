# Generated by Django 4.2.7 on 2023-11-15 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_berita_deskripsi'),
    ]

    operations = [
        migrations.AddField(
            model_name='berita',
            name='publikasi',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
