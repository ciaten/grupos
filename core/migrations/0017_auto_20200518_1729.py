# Generated by Django 2.2.12 on 2020-05-18 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_merge_20200518_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacao',
            name='descricao',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='informacao',
            name='imagem_infraestrutura',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]