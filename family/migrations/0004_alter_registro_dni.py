# Generated by Django 4.0.4 on 2022-05-25 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0003_alter_registro_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='dni',
            field=models.IntegerField(),
        ),
    ]