# Generated by Django 2.2.12 on 2020-05-18 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200518_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informacao',
            old_name='projetos',
            new_name='portifolio',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='pesquisadores',
        ),
    ]