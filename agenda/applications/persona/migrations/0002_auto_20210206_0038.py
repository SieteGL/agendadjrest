# Generated by Django 3.1.6 on 2021-02-06 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['-created'], 'verbose_name': 'Persona', 'verbose_name_plural': 'Personas'},
        ),
    ]