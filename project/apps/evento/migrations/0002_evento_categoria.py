# Generated by Django 4.2.3 on 2023-07-11 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='categoria',
            field=models.TextField(default='futbol'),
            preserve_default=False,
        ),
    ]