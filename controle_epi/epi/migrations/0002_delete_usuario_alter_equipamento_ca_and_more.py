# Generated by Django 5.1 on 2024-09-29 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epi', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='ca',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='validade',
            field=models.IntegerField(max_length=100),
        ),
    ]